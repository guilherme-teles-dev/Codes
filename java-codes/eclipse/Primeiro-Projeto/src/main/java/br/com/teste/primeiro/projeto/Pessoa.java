package br.com.teste.primeiro.projeto;

public class Pessoa {
	public String nome;
	private String telefone;
	private int idade;
	public Pessoa(String nome, String telefone, int idade){
		this.nome = nome;
		this.telefone = telefone;
		this.idade = idade;
	}
	public void estudar() {
		System.out.println("Estudando");
	}
	public void estudar(String disciplina) {
		System.out.println("Estudando" + disciplina);
	}
	public String getNome() {
		return nome;
	}
	public void setNome(String nome) {
		this.nome = nome;
	}
	public String getTelefone() {
		return telefone;
	}
	public void setTelefone(String telefone) {
		this.telefone = telefone;
	}
	public int getIdade() {
		return idade;
	}
	public void setIdade(int idade) {
		this.idade = idade;
	}
	
}
