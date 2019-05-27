import Cliente
import finalizadorNFCE
import finalizadorECF
import LancarProduto
import Impressao

def vendaDinheiroecf():
  LancarProduto.LancarProdutoSequencia()
  finalizadorECF.Dinheiroecf()
  Impressao.imprimir()
  
def vendaCrediarioecf():
  LancarProduto.LancarProdutoSequencia()
  finalizadorECF.Crediarioecf()
  Impressao.imprimir()

def vendaDinheiroNfce():
  LancarProduto.LancarProdutoSequencia()
  finalizadorNFCE.dinheiroNfce()
  Impressao.imprimir()
  
def vendaDebitoNfce():
  LancarProduto.LancarProdutoSequencia()
  finalizadorNFCE.debitoNfce()
  Impressao.imprimir()
  
def vendaCreditoNfce():
  LancarProduto.LancarProdutoSequencia()
  finalizadorNFCE.CreditoNfce()
  Impressao.imprimir()
  
def vendaCrediarioNfce():
  LancarProduto.LancarProdutoSequencia()
  finalizadorNFCE.crediarioNfce()
  Impressao.imprimir()
  
def vendaDinheiroNfceCpf():
  LancarProduto.LancarProdutoSequencia()
  Cliente.informarCliente()
  finalizadorNFCE.dinheiroNfce()
  Impressao.imprimir()