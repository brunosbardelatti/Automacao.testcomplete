﻿def LancarProdutoSequenciaEcf():
  cod =3001
  while cod < 3004:
   Aliases.HiperPdv.HwndSource_MainWindow.MainWindow.TabPrincipal.txtEntradaDados.SetText(cod)
   Aliases.HiperPdv.HwndSource_MainWindow.MainWindow.TabPrincipal.txtEntradaDados.Keys("[Enter]")
   Aliases.HiperPdv.HwndSource_MainWindow.MainWindow.TabPrincipal.numQuantidade.Keys("[Enter]")
   Aliases.HiperPdv.HwndSource_MainWindow.MainWindow.TabPrincipal.numValorTotalItem.Keys("[Enter]")
   cod = cod + 1
   Delay(2000)
   
def LancarProdutoSequenciaNfce():
  cod =3001
  while cod < 3004:
   Aliases.HiperPdv.HwndSource_MainWindow.MainWindow.TabPrincipal.txtEntradaDados.SetText(cod)
   Aliases.HiperPdv.HwndSource_MainWindow.MainWindow.TabPrincipal.txtEntradaDados.Keys("[Enter]")
   if (Aliases.HiperPdv.HwndSource_BaseWindow.BaseWindow.cboPessoa.Exists):
    Aliases.HiperPdv.HwndSource_BaseWindow.BaseWindow.cboPessoa.Keys("[Esc]")
   Aliases.HiperPdv.HwndSource_MainWindow.MainWindow.TabPrincipal.numQuantidade.Keys("[Enter]")
   Aliases.HiperPdv.HwndSource_MainWindow.MainWindow.TabPrincipal.numValorTotalItem.Keys("[Enter]")
   cod = cod + 1
   
def LancarProdutoSequenciaNfceCpf():
  cod =3001
  while cod < 3004:
   Aliases.HiperPdv.HwndSource_MainWindow.MainWindow.TabPrincipal.txtEntradaDados.SetText(cod)
   Aliases.HiperPdv.HwndSource_MainWindow.MainWindow.TabPrincipal.txtEntradaDados.Keys("[Enter]")
   if(Aliases.HiperPdv.HwndSource_BaseWindow.BaseWindow.cboPessoa.Exists):
    Aliases.HiperPdv.HwndSource_BaseWindow.BaseWindow.cboPessoa.Keys("[Enter]")
    Aliases.HiperPdv.HwndSource_BaseWindow.BaseWindow.mtbCpf.SetText("061.016.809-67")
    Aliases.HiperPdv.HwndSource_BaseWindow.BaseWindow.mtbCpf.Keys("[Enter]")
    Aliases.HiperPdv.HwndSource_BaseWindow.BaseWindow.txtNome.Keys("[F3]")
   else:
    Aliases.HiperPdv.HwndSource_MainWindow.MainWindow.TabPrincipal.txtEntradaDados.Keys("[F2]")
    Aliases.HiperPdv.HwndSource_BaseWindow.BaseWindow.cboPessoa.Keys("[Enter]")
    Aliases.HiperPdv.HwndSource_BaseWindow.BaseWindow.mtbCpf.SetText("061.016.809-67")
    Aliases.HiperPdv.HwndSource_BaseWindow.BaseWindow.mtbCpf.Keys("[Enter]")
    Aliases.HiperPdv.HwndSource_BaseWindow.BaseWindow.txtNome.Keys("[F3]")
    Aliases.HiperPdv.HwndSource_MainWindow.MainWindow.TabPrincipal.numQuantidade.Keys("[Enter]")
    Aliases.HiperPdv.HwndSource_MainWindow.MainWindow.TabPrincipal.numValorTotalItem.Keys("[Enter]")
   Aliases.HiperPdv.HwndSource_MainWindow.MainWindow.TabPrincipal.numQuantidade.Keys("[Enter]")
   Aliases.HiperPdv.HwndSource_MainWindow.MainWindow.TabPrincipal.numValorTotalItem.Keys("[Enter]")
   cod = cod + 1


   
