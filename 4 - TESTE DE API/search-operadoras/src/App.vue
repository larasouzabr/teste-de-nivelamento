<template>
  <v-responsive class="mx-auto mb-3" max-width="900">
    <h1 class="mb-3 font">Dados cadastrais das Operadoras Ativas na ANS</h1>
    <v-text-field
      label="Operadoras Ativas"
      hide-details="auto"
      v-model="termoBusca"
      variant="solo"
      @keyup.enter="buscar"
      class="mb-5"
    ></v-text-field>

    <v-data-table
      class="table"
      :items="termoBusca ? dados : dadosGerais"
      :headers="columns"
    ></v-data-table>
  </v-responsive>
</template>

<script>
import { fetchData, getDados } from "../src/service/data.ts";

export default {
  data() {
    return {
      termoBusca: "",
      dados: [],
      dadosGerais: [],
      columns: [
        { title: "CNPJ", value: "cnpj", align: "center" },
        { title: "Razão Social", value: "razao_social", align: "center" },
        {
          title: "Modalidade",
          value: "modalidade",
          align: "end",
          key: "modalidade",
        },
        { title: "Cidade", value: "cidade", align: "end", key: "cidade" },
        { title: "UF", value: "uf", align: "end", key: "uf" },
      ],
    };
  },
  created() {
    this.getDadosGerais();
  },
  methods: {
    async buscar() {
      try {
        this.dados = await fetchData(this.termoBusca);
        console.log("Dados encontrados:", this.dados);
      } catch (error) {
        console.error("Erro ao buscar dados:", error);
      }
    },
    async getDadosGerais() {
      try {
        this.dadosGerais = await getDados();
        console.log("Dados gerais encontrados:", this.dadosGerais);
      } catch (error) {
        console.error("Erro ao buscar dados gerais:", error);
      }
    },
  },
};
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
.v-data-table__th {
  background-color: #c8a4f4;
  font-family: wfont_d720ea_51310c14aaf84b37ac8aa32d055dc8c1, wf_51310c14a;
  font-size: 20px;
}

.font {
  font-family: wfont_d720ea_51310c14aaf84b37ac8aa32d055dc8c1, wf_51310c14a;
}
tbody {
  background-color: #ffffff;
}
</style>
