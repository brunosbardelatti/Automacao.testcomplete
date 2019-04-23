import finalizadorNFCE
import finalizadorECF
import LancarProduto

def vendaDinheiroecf():
  LancarProduto.LancarProdutoSequenciaEcf()
  FinalizadorECF.Dinheiroecf()
  
def vendaCrediarioecf():
  LancarProduto.LancarProdutoSequenciaEcf()
  FinalizadorECF.Crediarioecf()

def vendaDinheiroNfce():
  LancarProduto.LancarProdutoSequenciaNfce()
  finalizadorNFCE.dinheiroNfce()
  
def vendaDebitoNfce():
  LancarProduto.LancarProdutoSequenciaNfce()
  finalizadorNFCE.debitoNfce()
  
def vendaCreditoNfce():
  LancarProduto.LancarProdutoSequenciaNfce()
  finalizadorNFCE.CreditoNfce()
  
def vendaCrediarioNfce():
  LancarProduto.LancarProdutoSequenciaNfce()
  finalizadorNFCE.vendaCrediario()
  
def vendaDinheiroNfceCpf():
  LancarProduto.LancarProdutoSequenciaNfceCpf()
  finalizadorNFCE.dinheiroNfce()