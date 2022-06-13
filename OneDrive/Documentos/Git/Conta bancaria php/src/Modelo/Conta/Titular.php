<?php

namespace Gabriel\Banco\Modelo\Conta;

use Gabriel\Banco\Modelo\Pessoa;
use Gabriel\Banco\Modelo\Cpf;
use Gabriel\Banco\Modelo\Endereco;

class Titular extends Pessoa
{
    private $endereco;

    public function __construct(Cpf $Cpf, string $nome, Endereco $endereco)
    {
        parent::__construct($nome, $Cpf);
        $this->endereco = $endereco;
    }

    public function recuperarEndereco(): Endereco
    {
        return $this->endereco;
    }
}