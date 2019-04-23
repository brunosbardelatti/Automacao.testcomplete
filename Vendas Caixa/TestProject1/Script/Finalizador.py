def Dinheiroecf():
  Aliases.HiperPdv.HwndSource_MainWindow.MainWindow.TabPrincipal.btnSubtotalVenda.ClickButton()
  Aliases.HiperPdv.HwndSource_MainWindow.MainWindow.TabPrincipal.edtConsoleInput.Keys("[F1]")
  Aliases.HiperPdv.HwndSource_MainWindow.MainWindow.TabPrincipal.edtConsoleInput.Keys("[Enter]")
  Aliases.HiperPdv.HwndSource_MainWindow.MainWindow.TabPrincipal.btnConfirmar.Keys("[Enter]")
  
def Crediarioecf():
  hiperPdv = Aliases.HiperPdv
  hwndSource = hiperPdv.HwndSource_MainWindow
  tabControl = hwndSource.MainWindow.TabPrincipal
  tabControl.Click(569, 382)
  tabControl.txtEntradaDados.Keys("[F3]")
  hiperTextBox = tabControl.edtConsoleInput
  hiperTextBox.Keys("[F8]")
  hiperTextBox.Keys("[F4]")
  baseWindow = hiperPdv.HwndSource_BaseWindow.BaseWindow
  baseWindow.TxtFiltro.Keys("[F5]")
  baseWindow.DgrEntidades.DblClickCell(0, "Nome")
  hiperTextBox.Keys("[Enter]")
  baseWindow.btnContinuar.Keys("[F3]")
  hiperTextBox.Keys("[Enter]")
  hiperTextBox.Keys("[Enter]")
  hiperTextBox.Keys("2")
  hiperTextBox.Keys("[Enter]")
  tabControl.btnConfirmar.Keys("[Enter]")
  baseWindow.btnSim.Keys("[Enter]")
  hiperPdv.HwndSource_BaseWindow2.BaseWindow.dgvPendencias.Datagridcell1.Keys("[F3]")
  hwndSource.Activate()
  
  

