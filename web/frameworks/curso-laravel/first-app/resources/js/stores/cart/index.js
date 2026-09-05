import { defineStore } from "pinia";
import state from "./state";
import actions from "./actions";

export const useCarritoStore = defineStore('carrito', {
    state,
    actions,
});