from django.shortcuts import render

# Create your views here.

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

responseDicts = {
    'get_afiliado': {
        "Documento": "#########",
        "TipoDocumento": "C",
        "Nombres": "test test",
        "Bodega": "5119",
        "Fuerza": "5",
        "FuerzaNombre": None,
        "Sexo": "M",
        "FechaNacimiento": "1900/01/01",
        "IDCotizante": "1234567",
        "Estafiliacion": "Activo",
        "Descripcion": "Cotizante",
        "Celular": "3000000000",
        "NombreEsm": "COMANDO AÉREO DE TRANSPORTE MILITAR",
        "EstadoAfiliacion": "Activo",
        "Estado": 1
    },
    'get_stado': {
        "Documento": "#########",
        "TipoDocumento": "R",
        "Estado": "Activo"
    },
    'get_personal': {
        "TipoDocumento": "C",
        "Documento": "#######",
        "Nombres": "XXXXX XXXXX XXXXX XXXXX", "Fecha": "2020/05/14 17:00", "Estado": "Activo para formular",
        "Observacion": "",
        "Vinculaciones": [
            {
                "CodEstablecimiento": "5119",
                "Establecimiento": "COMANDO AÉREO DE TRANSPORTE MILITAR",
                "Especialidad": "Medicina General - SSFM",
                "IdEspecialidad": None,
                "SiglaEspecialidad": None,
                "ClasificacionEspecialidad": "GENERAL",
                "TipoContrato": "Militar",
                "Formula": "Si"
            }]
    }
}


class GetAffiliate(APIView):

    def get(self, request, *args, **kwargs):
        response = responseDicts['get_afiliado']
        params = request.query_params.dict()
        response['Documento'] = params['documento']
        response['TipoDocumento'] = params['tipoDocumento']
        return Response(data=response, status=status.HTTP_200_OK)


class GetAffiliateStateByDate(APIView):

    def get(self, request, *args, **kwargs):
        response = responseDicts['get_stado']
        params = request.query_params.dict()
        response['Documento'] = params['documento']
        response['TipoDocumento'] = params['tipoDocumento']
        return Response(response, status=status.HTTP_200_OK)


class GetStaff(APIView):

    def get(self, request, *args, **kwargs):
        response = responseDicts['get_personal']
        params = request.query_params.dict()
        response['Documento'] = params['documento']
        response['TipoDocumento'] = params['tipoDocumento']
        return Response(response, status=status.HTTP_200_OK)


def test(matrix):
    n = matrix.__len__()
    total_amount = 0
    if n < 4:
        return 0
    else:
        row = ''
        other = dict()
        column = dict()
        for i in range(n):
            for j in range(n):
                if i not in other:
                    other[i] = {j: dict(dec=matrix[i][j], inc=matrix[i][j])}
                if j not in other[i]:
                    other[i][j] = dict(dec=matrix[i][j], inc=matrix[i][j])
                if j not in column:
                    column[j] = matrix[i][j]
                else:
                    if matrix[i][j] not in column[j]:
                        column[j] = matrix[i][j]
                    else:
                        column[j] += matrix[i][j]
                    if column[j].__len__() > 3:
                        total_amount += 1
                        column[j] = matrix[i][j]
                if i - 1 in other:
                    if j - 1 in other[i - 1]:
                        if matrix[i][j] not in other[i - 1][j - 1]['dec']:
                            other[i][j]['dec'] = matrix[i][j]
                        else:
                            other[i][j]['dec'] = other[i - 1][j - 1]['dec'] + matrix[i][j]
                        if other[i][j]['dec'].__len__() > 3:
                            total_amount += 1
                            other[i][j]['dec'] = matrix[i][j]
                    if j + 1 in other[i - 1]:
                        if matrix[i][j] not in other[i - 1][j + 1]['inc']:
                            other[i][j]['inc'] = matrix[i][j]
                        else:
                            other[i][j]['inc'] = other[i - 1][j + 1]['inc'] + matrix[i][j]
                        if other[i][j]['inc'].__len__() > 3:
                            total_amount += 1
                            other[i][j]['inc'] = matrix[i][j]
                if matrix[i][j] not in row:
                    row = matrix[i][j]
                else:
                    row += matrix[i][j]
                if row.__len__() > 3:
                    total_amount += 1
                    row = matrix[i][j]
        return total_amount


already_tested = dict()
