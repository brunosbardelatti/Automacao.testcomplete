def LancarProdutoSequencia():
  cod =3001
  while cod < 3004:
   Aliases.HiperPdv.HwndSource_MainWindow.MainWindow.TabPrincipal.txtEntradaDados.SetText(cod)
   Aliases.HiperPdv.HwndSource_MainWindow.MainWindow.TabPrincipal.txtEntradaDados.Keys("[Enter]")
   if (Aliases.HiperPdv.HwndSource_BaseWindow.BaseWindow.cboPessoa.Exists):
    Aliases.HiperPdv.HwndSource_BaseWindow.BaseWindow.cboPessoa.Keys("[Esc]")
   Aliases.HiperPdv.HwndSource_MainWindow.MainWindow.TabPrincipal.numQuantidade.Keys("[Enter]")
   Aliases.HiperPdv.HwndSource_MainWindow.MainWindow.TabPrincipal.numValorTotalItem.Keys("[Enter]")
   cod = cod + 1
   
