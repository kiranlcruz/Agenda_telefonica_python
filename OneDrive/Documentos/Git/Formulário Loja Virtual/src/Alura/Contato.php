<?php

namespace App\Alura;

class Contato
{

    private $email;
    private $endereco;
    private $cep;
    private $telefone;

    public function __construct(string $email, string $endereco, string $cep, string $telefone)
    {
        $this->email = $email;

        if ($this->validaEmail ($email) !== false) {
            $this->validaEmail($email);
        } else {
            $this->validaEmail("Email inválido");
        }

        $this->endereco = $endereco;
        $this->cep = $cep;

        if ($this->validaTelefone($telefone)) {
            $this->setTelefone($telefone);

        } else {
            $this->telefone = "Telefone inválido";
        }
        
    }

    private function validaTelefone(string $telefone): int
    {
        //6666-666 começa com número, em quatro grupos, barra
        return preg_match('/^[0-9]{4}-[0-9]{4}$/', $telefone, $encontrados);
    }

    private function setTelefone(string $telefone): void
    {
        $this->telefone = $telefone;
    }

    private function setEmail(string $email): void
    {
        $this->$email = $email;     
    }

    public function getUsuario(): string
    {
        $posicaoArroba = strpos($this->email, "@");

        if ($posicaoArroba === false) {
            return "Usuario Inválido";
        }

        return substr($this->email, 0, $posicaoArroba);
    }

    private function validaEmail(string $email)
    {
        return filter_var($email, FILTER_VALIDATE_EMAIL);
    }

    public function getEmail(): string
    {
        return $this->email;
    }

    public function getEnderecoCep(): string
    {
        $enderecoCep = [$this->endereco, $this->cep]; ##virou array
        return implode(" - ", $enderecoCep); 
    }

    public function getTelefone(): string
    {
        return $this->telefone;
    }
}