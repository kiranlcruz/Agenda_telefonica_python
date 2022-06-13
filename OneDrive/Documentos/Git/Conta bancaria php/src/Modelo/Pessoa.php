<?php

namespace Gabriel\Banco\Modelo;

class Pessoa
{
    protected $nome;
    private $Cpf;

    public function __construct(string $nome, Cpf $Cpf)
    {
        $this->validarNomeTitular($nome);
        $this->nome = $nome;
        $this->Cpf = $Cpf;
    }

    public function recuperarNome(): string
    {
        return $this->nome;
    }

    public function recuperarCpf(): string
    {
        return $this->Cpf->recuperarNumero();
    }

    protected function validarNomeTitular(string $nomeTitular)
    {
        if (strlen($nomeTitular) < 5) {
            echo "Nome precisa ter pelo menos 5 caracteres";
            exit();
        }
    }
}

