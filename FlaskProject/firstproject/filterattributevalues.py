import json

# List of codes to filter by
filter_codes = [
    'tipo_de_producto',
    'Modelo',
    'mod_procesador',
    'velocidad_procesador',
    'sistema_operativo_lov',
    'megapixeles_camara_trasera',
    'accesibilidad',
    'capacidad_de_la_bateria',
    'resist_al_agua',
    'condicion_de_producto',
    'vida_util_promedio_segun_uso_esperado',
    'disponibilidad_repuestos_servicio_tecnico',
    'tipo_de_pantalla',
    'memoria_ram',
    'me_interna',
    'carga_inalambrica',
    'pantalla_pulgadas',
    'material_blandos',
    'lector_de_huella_digital',
    'memoria_expandible',
    'largo_cable_mt',
    'tipo_de_bateria',
    'tipo_de_memoria_ram_lov',
    'frecuencia_memoria_ram',
    'ram_expandible',
    'resolucion_pantalla',
    'pantalla_touch',
    'tarjeta_video_integrada',
    'disco_duro',
    'disco_solido',
    'cantidad_puertos_usb',
    'numero_puertos_hdmi',
    'conexion_ethernet',
    'nfc',
    'gps',
    'bluetooth',
    'cantidad_de_camaras',
    'operador',
    'carga_rapida',
    'usb',
    'tipo_de_memoria_ram_lov',
    'tipo_panel',
    'tarjeta_video_dedicada',
    'lector_tarjeta_memoria',
    'alimentacion',
    'entrada_de_audio',
    'tipo_de_audifono',
    'tipo_de_conector',
    'inalambrico',
    'microfono',
    'duracion_bateria_hr',
    'entrada_para_microfono',
    'material_pulsera',
    'compatibilidad',
    'resolucion_salida_video',
    'compatibilidad_pulgadas',
    'tipo_de_brazo_pantalla',
    'peso_max_permitido_kg',
    'tipo_instrumento'
]

input_file = "FlaskProject/firstproject/attrval.json"
output_file = "filtered_attribute_values.json"

# Read JSON data from file
with open(input_file, 'r', encoding='utf-8') as f:
    json_data = json.load(f)

# Filter values_lists by code in filter_codes
filtered = [item for item in json_data.get("values_lists", []) if item.get("code") in filter_codes]

# Prepare output structure
output_data = {
    "values_lists": filtered
}

# Write filtered JSON to output file
with open(output_file, 'w', encoding='utf-8') as f:
    json.dump(output_data, f, ensure_ascii=False, indent=2)

print(f"Filtered data saved to '{output_file}'")
