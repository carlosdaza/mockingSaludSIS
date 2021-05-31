from django.shortcuts import render

# Create your views here.

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

responseDicts = {
    'get_formulacion': {
        "CodigoEsmAtencion": "110018508080",
        "NombreEsmAtencion": "DISPENSARIO MEDICO GILBERTO ECHEVERRY MEJIA",
        "FuerzaAfiliadoSigla": "EJC",
        "FuerzaAfiliado": "Ejercito Nacional de Colombia",
        "FuerzaAfiliadoCod": "3",
        "TipoDocAfiliacionSigla": "CC",
        "TipoDocAfiliacion": "Cédula de ciudadanía",
        "DocumentoPaciente": "#######",
        "NombrePaciente": "XXXXX  XXXXXX XXXXXX ",
        "SiglaEsmAdscrito": "ESM DMCAL",
        "NombreEsmAdscrito": "DISPENSARIO MEDICO CALI",
        "Tipoafiliacion": "Cotizante",
        "Codtipoafiliacion": "1",
        "EstadoAfiliado": "Activo",
        "EstadoAfiliacionSigla": "AC",
        "Genero": "Masculino",
        "EstadoCivil": "Unión libre",
        "Grado": "SLP",
        "CausaExternaSigla": "EG",
        "CausaExerna": "Enfermedad general",
        "FechaFormulacion": "16-03-2016 17:15",
        "ConsecutivoFormula": "E2016001####",
        "TipoFormulacionSigla": "FNE",
        "TipoFormulacion": "Formulación no especial",
        "TipoDocMedico": "CC",
        "TipoDocMedicoNombre": "Cédula de ciudadanía",
        "NumeroDocMedico": "#######",
        "NombreMedico": "XXXXXX XXXXXX XXXXX ",
        "EspecialidadMedico": "",
        "CodigoCie10": "L519",
        "DescripcionCie10": "ERITEMA MULTIFORME, NO ESPECIFICADO",
        "List": [
            {
                "CodigoSsmpMedicamento": "3470010",
                "NombreGenericoMedicamento": "BETAMETASONA DIPROPIONATO+CLOTRIMAZOL",
                "ConcentracionMedicamento": "(0.05+1)%",
                "CantidadFormulada": 2.0,
                "FormaFarmaceutica": "Crema tópica",
                "Dosis": None
            }]
    }

}


class GetFiling(APIView):

    def get(self, request, *args, **kwargs):
        response = responseDicts['get_formulacion']
        params = request.query_params.dict()
        response['ConsecutivoFormula'] = params['Id']
        return Response(response, status=status.HTTP_200_OK)
