class FirstExecutorLogic:
    def __init__(self):
        pass

    def run(self, input_data: dict):
        # Şemadaki Ex1Inputs modeline uygun olarak 'in1' alanını alıyoruz
        in1_obj = input_data.get("in1", {})

        # Gelen verinin dictionary veya direkt değer olma durumunu güvenli bir şekilde kontrol ediyoruz
        val = in1_obj.get("value", "") if isinstance(in1_obj, dict) else in1_obj

        # Şemadaki Ex1Outputs bizden 'out1' (TextField) bekliyor.
        # Platformdaki katı Pydantic doğrulamalarından (validation) geçmesi için tam obje formatında dönüyoruz.
        return {
            "out1": {
                "name": "MetinAlani",
                "value": f"FirstExecutor işledi: {val}",
                "type": "string",
                "field": "textInput"
            }
        }


class SecondExecutorLogic:
    def __init__(self):
        pass

    def run(self, input_data: dict):
        # Şemadaki Ex2Inputs modeline uygun olarak 'in1' ve 'in2' alanlarını alıyoruz
        in1_obj = input_data.get("in1", {})
        in2_obj = input_data.get("in2", {})

        val1 = in1_obj.get("value", "") if isinstance(in1_obj, dict) else in1_obj
        val2 = in2_obj.get("value", 0.0) if isinstance(in2_obj, dict) else in2_obj

        # Çıktı üretecek iş mantığı işlemleri
        result_text = f"SecondExecutor -> Giriş Metni: {val1}"
        result_number = float(val2) * 2  # Örnek bir matematiksel işlem

        # Şemadaki Ex2Outputs bizden hem 'out1' (TextField) hem de 'out2' (NumberField) bekliyor.
        return {
            "out1": {
                "name": "MetinAlani",
                "value": result_text,
                "type": "string",
                "field": "textInput"
            },
            "out2": {
                "name": "SayiAlani",
                "value": result_number,
                "type": "number",
                "field": "textInput"
            }
        }