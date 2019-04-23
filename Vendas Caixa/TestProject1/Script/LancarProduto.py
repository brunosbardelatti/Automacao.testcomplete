def LancarProdutoSequencia():
  cod =3001
  while cod < 3004:
   Aliases.HiperPdv.HwndSource_MainWindow.MainWindow.TabPrincipal.txtEntradaDados.SetText(cod)
   Aliases.HiperPdv.HwndSource_MainWindow.MainWindow.TabPrincipal.txtEntradaDados.Keys("[Enter]")
   Aliases.HiperPdv.HwndSource_MainWindow.MainWindow.TabPrincipal.numQuantidade.Keys("[Enter]")
   Aliases.HiperPdv.HwndSource_MainWindow.MainWindow.TabPrincipal.numValorTotalItem.Keys("[Enter]")
   cod = cod + 1
   Delay(2000)