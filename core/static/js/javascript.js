function validar (){
    var nome = registration.pnome.value;
    var sobrenome = registration.unome.value;
    var email = registration.email.value;
    var celular = registration.celular.value;
    var nascimento = registration.nascimento.value;      
    var cpf = registration.cpf.value;
    var login = registration.login.value;
    var senha = registration.senha.value;
    var confirm_senha = registration.conf_senha.value;
    var re_cpf = new RegExp("^([0-9]{2}[\.][0-9]{3}[\.][0-9]{3}[-][0-9]{2})$|^([0-9]{3}[\.][0-9]{3}[\.][0-9]{3}[-][0-9]{2})$");
   	var re_senha = new RegExp("^(?=.*[0-9])(?=.*[a-z])(?=.*[A-Z]).+$");

if (nome ==""){
    alert('Preencha o campo com o seu nome');
    registration.nome.focus();
    return false;
  }
else if (sobrenome ==""){
     alert('Preencha o campo com o seu sobrenome');
     registration.sobrenome.focus();
     return false;
}
else if (email ==""){
     alert('Preencha o campo com o seu email');
     registration.email.focus();
     return false;
}
else if (nascimento ==""){
     alert('Preencha o campo com a sua data de nascimento');
     registration.nascimento.alert();
     return false
}
else if (nascimento !=""){
  if  (2018 - nascimento < 18){
    alert("Você deve ter mais de 18 anos.");
    return false;
  }
}
else if (cpf ==""){
     alert('Preencha o campo com o seu cpf');
     return false;
}

else if (cpf !=""){
	if (re_cpf.test(cpf)){
	}
	else{
		alert('Cpf Invalido')
		registration.cpf.focus();
     	return false;
	}
}

else if (login ==""){
     alert('Digite o campo com o seu login');
     registration.login.focus();
     return false;
}
else if (senha ==""){
     alert('Digite o campo com a sua senha')
     registration.senha.focus();
     return false;
}
else if (confirm_senha ==""){
     alert('Digite o campo confirmando a sua senha')
     registration.confirm_senha.focus();
     return false;
}
if (senha != confirm_senha){
    alert('As senhas não coincidem')
    registration.confirm_senha().focus;
    return false;
}

else if (senha !=""){
	if (re_senha.test(senha)){

	}
	else{
		alert('Senha invalida, o campo deve possuir uma letra e um número')
		registration.cpf.focus();
     	return false;
	}
  }

}

//Validação na submissão
document.getElementById("formulario").onsubmit = function(event){
  var aprovado = 0;
  var cancelado = 0;
  var valueCampo = document.getElementsByClassName("check");
  if (valueCampo.length < 40 ){
      alert("O mínimo permitido é de 20 alunos");
      return false;
  }else if(valueCampo.length > 120){
      alert("O máximo permitido é de 60 alunos");
  }else {
      for (var i = 0; i< valueCampo.length ; i += 2){
          if (valueCampo[i].checked == false && valueCampo[i+1].checked == false ){
              alert("Todos os campos devem ser preenchidos");
              return false;
          }
      }
      for (var i = 0; i < valueCampo.length; i++){
          if(valueCampo[i].checked == true ){
              if(valueCampo[i].value == "aprovado"){
                  aprovado++;
              }else{
                  cancelado++;
              }
          }
      }
      alert("Aprovados: "+aprovado+"\nCancelados: "+cancelado);
      return window.confirm("Deseja enviar o formulário ?");
  }
}
