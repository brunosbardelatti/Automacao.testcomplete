import time 
def login():
  BuiltIn.ShowMessage("certifiquese que o caixa está configurada, para o correto cupom fiscal a ser executado.")
  TestedApps.HiperPdv.Run()
  time.sleep(1)
  #-------------Inserir o Usuario correto para Logar----------------------------------------------------------
  Aliases.HiperPdv.HwndSource_MainWindow.MainWindow.TabPrincipal.txtUsuario.SetText("nfce")
  #-------------Inserir o senha  correto para Logar-----------------------------------------------------------
  Aliases.HiperPdv.HwndSource_MainWindow.MainWindow.TabPrincipal.txtSenha.Keys("123")
  Aliases.HiperPdv.HwndSource_MainWindow.MainWindow.TabPrincipal.txtSenha.Keys("[Enter]")
