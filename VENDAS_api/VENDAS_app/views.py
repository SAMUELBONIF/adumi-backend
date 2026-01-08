
from rest_framework import viewsets, serializers
from .models import  Cliente, Produto, Venda, Itenvenda
from django.http import HttpResponse
from rest_framework.exceptions import ValidationError


def home(request):
    return HttpResponse("Bem-vindo à API ADUMI!")



# ================================ CLIENTE ================================== 

# Serializador para o modelo
class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'

# ViewSet para o modelo
class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer


# ================================ PRODUTO ================================== 
# Serializador para o modelo
class ProdutoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produto
        fields = '__all__'

# ViewSet para o modelo
class ProdutoViewSet(viewsets.ModelViewSet):
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer

    def perform_destroy(self, instance):
        try:
            instance.delete()
        except ProtectedError:
            raise ValidationError(
                "Este produto não pode ser apagado pois está associado a uma venda."
            )


# ================================ VENDA ==================================
# Serializador para o modelo
class VendaSerializer(serializers.ModelSerializer):
    cliente_nome = serializers.CharField(source='cliente.nome', read_only=True)
    produto_nome = serializers.CharField(source='produto.nome', read_only=True)

    class Meta:
        model = Venda
        fields = [
            'id',
            'cliente',
            'cliente_nome',
            'produto',
            'produto_nome',
            'quantidade',
            'valortotal'
        ]


# ViewSet para o modelo
class VendaViewSet(viewsets.ModelViewSet):
    queryset = Venda.objects.all()
    serializer_class = VendaSerializer


# ================================ ITENVENDA ==================================
# Serializador para o modelo



class ItemVendaSerializer(serializers.ModelSerializer):
    # Para GET: objetos aninhados com nome e id
    venda_info = serializers.SerializerMethodField()
    produto_info = serializers.SerializerMethodField()

    class Meta:
        model = Itenvenda
        fields = [
            'id',
            'venda',          # FK para POST/PUT
            'produto',        # FK para POST/PUT
            'venda_info',     # Apenas leitura
            'produto_info',   # Apenas leitura
            'preco_unitario',
            'quantidade',
            'subtotal'
        ]

    # GET / READ
    def get_venda_info(self, obj):
        return {
            "id": obj.venda.id,
            "cliente": obj.venda.cliente.nome
        }

    def get_produto_info(self, obj):
        return {
            "id": obj.produto.id,
            "nome": obj.produto.nome
        }

      




# ViewSet para o modelo
class ItenvendaViewSet(viewsets.ModelViewSet):
    queryset = Itenvenda.objects.select_related(
        'produto',
        'venda',
        'venda__cliente'
        
    )
    serializer_class = ItemVendaSerializer

    # 1️⃣ Diminuir estoque ao CRIAR item de venda
    def perform_create(self, serializer):
        produto = serializer.validated_data['produto']
        quantidade = serializer.validated_data['quantidade']

        if produto.estoque < quantidade:
            raise ValidationError({
                "estoque": f"Estoque insuficiente. Disponível: {produto.estoque}"
            })

        produto.estoque -= quantidade
        produto.save()
        serializer.save()

    # 2️⃣ Devolver estoque ao EXCLUIR item
    def perform_destroy(self, instance):
        produto = instance.produto
        produto.estoque += instance.quantidade
        produto.save()
        instance.delete()

    # 3️⃣ Ajustar estoque ao ATUALIZAR quantidade
    def perform_update(self, serializer):
        instance = self.get_object()
        produto = instance.produto

        nova_quantidade = serializer.validated_data.get(
            'quantidade',
            instance.quantidade
        )

        diferenca = nova_quantidade - instance.quantidade  # ✅ CORRIGIDO

        if diferenca > 0 and produto.estoque < diferenca:
            raise ValidationError({
                "estoque": "Estoque insuficiente para esta alteração."
            })

        produto.estoque -= diferenca
        produto.save()
        serializer.save()




