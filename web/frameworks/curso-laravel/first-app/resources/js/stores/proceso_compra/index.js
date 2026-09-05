import { defineStore } from "pinia";
import state from "./state";
import actions from "./actions";

export const useProcesoCompraStore = defineStore('proceso_compra', {
    state,
    actions,
});