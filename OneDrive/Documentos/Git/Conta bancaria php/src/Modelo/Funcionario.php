<?php

namespace Gabriel\Banco\Modelo;

class Funcionario extends Pessoa
{
    private $cargo;

    public function __construct(string $nome, Cpf $Cpf, string $cargo)
    {
        parent::__construct($nome, $Cpf);
        $this->cargo = $cargo;
    }

    public function recuperarCargo(): string
    {
        return $this->cargo;

    }
    public function alterarNome(string $nome): void
    {
        $this->validarNomeTitular($nome);
    }
    
}