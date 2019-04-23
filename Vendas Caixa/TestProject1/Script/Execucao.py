import Cliente
import finalizadorNFCE
import finalizadorECF
import LancarProduto

def vendaDinheiroecf():
  LancarProduto.LancarProdutoSequencia()
  FinalizadorECF.Dinheiroecf()
  
def vendaCrediarioecf():
  LancarProduto.LancarProdutoSequencia()
  FinalizadorECF.Crediarioecf()

def vendaDinheiroNfce():
  LancarProduto.LancarProdutoSequencia()
  finalizadorNFCE.dinheiroNfce()
  
def vendaDebitoNfce():
  LancarProduto.LancarProdutoSequencia()
  finalizadorNFCE.debitoNfce()
  
def vendaCreditoNfce():
  LancarProduto.LancarProdutoSequencia()
  finalizadorNFCE.CreditoNfce()
  
def vendaCrediarioNfce():
  LancarProduto.LancarProdutoSequencia()
  finalizadorNFCE.vendaCrediario()
  
def vendaDinheiroNfceCpf():
  LancarProduto.LancarProdutoSequencia()
  Cliente.informarCliente()
  finalizadorNFCE.dinheiroNfce()