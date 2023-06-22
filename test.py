from main import main

import numpy as np
import matplotlib.pyplot as plt


def test(url):#独立して実行
    res,status_code=main(url,save_pickle=True)
    if status_code==200:
        print("===>",res["channel_title"],res["video_title"])

if __name__ == "__main__":

    test("https://www.youtube.com/watch?v=m72Szuvir2w",save_pickle=True,save_firestore=False)

    # #ids=['UCoSrY_IQQVpmIRZ9Xf-y93g', 'UC4YaOt1yT-ZeyB0OmxHgolA', 'UCCzUftO8KOVkV4wQG1vkUvg', 'UC1DCedRgGHBdm81E1llLhOQ', 'UCL_qhgtOy0dy1Agp8vkySQg', 'UCdn5BQ06XqgXoAxIhbqw5Rg', 'UCJFZiqLMntJufDCHc6bQixg', 'UChAnqc_AY5_I3Px5dig3X1Q', 'UC5CwaMl1eIgY8h02uZw7u8A', 'UC1opHUrw8rvnsadT-iGp7Cg', 'UC-hM6YJuNYVAmUWxeIr9FeA', 'UCgIfLpQvelloDi8I0Ycbwpg', 'UCyl1z3jo3XHR1riLFKG5UAg', 'UCdyqAaZDKHXg4Ahi7VENThQ', 'UCvaTdHTWBGv3MKj3KVqJVCw', 'UCSFCh5NL4qXrAy9u-u2lX3g', 'UCMwGHR0BTZuLsmjY_NT5Pwg', 'UCvzGlP9oQwU--Y0r9id_jnA', 'UCHsx4Hqa-1ORjQTh9TYDhww', 'UCO5Jvsc_sKuZi3MhnJxrlzQ', 'UCbFwe3COkDrbNsbMyGNCsDg', 'UC1CfXB_kRs3C-zaeTG3oGyg', 'UC7fk0CB07ly8oSl0aqKkqFg', 'UCS9uQI-jC3DE0L4IpXyvr6w', 'UCqm3BQLlJfvkTsX_hvm0UmA', 'UCX7YkU9nEeaoZbkVLVajcMg', 'UCZlDXzGoo7d44bwdNObFacg', 'UCQ0UDLQCjY0rmuxCDE38FGg', 'UCUKD-uaobj9jiqB-VXt71mA', 'UCP0BspO_AMEe3aQqqpo89Dg', 'UCYz_5n-uDuChHtLo7My1HnQ', 'UC1uv2Oq6kNxgATlCiez59hw', 'UCspv01oxUFf_MTSipURRhkA', 'UCFKOVgVbGmX65RxO3EtH3iw', 'UCXTpFs_3PqI41qX2d9tL2Rw', 'UCK9V2B22uJYu3N7eR_BT9QA', 'UCp-5t9SrOQwXMU7iIjQfARg', 'UCD-miitqNY3nyukJ4Fnf4_A', 'UCp6993wxpyDPHUpavwDFqgg', 'UCIBY1ollUsauvVi4hW4cumw', 'UCAWSyEs_Io8MtpY3m-zqILA', 'UCAWxPGGuIfWME2KTLUmSCHw', 'UCvInZx9h3jC2JzsIzoOebWg', 'UCENwRMx5Yh42zWpzURebzTw', 'UC1suqwovbL1kzsoaZgFZLKg', 'UC9V3Y3_uzU5e-usObb6IE1w', 'UCa9Y57gfeY0Zro_noHRVrnw', 'UCDqI2jOz0weumE8s7paEk6g', 'UC8NZiqKx6fsDT3AVcMiVFyA', 'UC6eWCld0KwmyHFbAqK3V-Rw', 'UCv1fFr156jc65EMiLbaLImw', 'UCQYADFw7xEJ9oZSM5ZbqyBw', 'UCoztvTULBYd3WmStqYeoHcA', 'UCD8HOxPs4Xvsm8H0ZxXGiBw', 'UChLfthKoUV502J7gU9STArg', 'UCOyYb1c43VlX9rc_lT6NKQw', 'UC6wvdADTJ88OfIbJYIpAaDA', 'UC0TXe_LYZ4scaW2XMyi5_kw', 'UCQ1U65-CQdIoZ2_NA4Z4F7A', 'UCHVXbQzkl3rDfsXWo8xi2qw', 'UCFTLzh12_nrtzqBPsTCqenA', 'UCZ1xuCK1kNmn5RzPYIZop3w', 'UC_vMYWcDjmfdpH6r4TTn1MQ', 'UChgTyjG-pdNvxxhdsXfHQ5Q', 'UCFv2z4iM5vHrS8bZPq4fHQQ', 'UCKMYISTJAQ8xTplUPHiABlA', 'UCXRlIK3Cw_TJIQC5kSJJQMg', 'UCs9_O1tRPMQTHQ-N_L6FU2g', 'UCdpUojq0KWZCN9bxXnZwz5w', 'UCPLeqi7rIqS9uY4_TrSUOMg', 'UCb5JxV6vKlYVknoJB8TnyYg', 'UC0g1AE0DOjBYnLhkgoRWN1w', 'UCAoy6rzhSf4ydcYjJw3WoVg', 'UCsg-YqdqQ-KFF0LNk23BY4A', 'UCMYtONm441rBogWK_xPH9HA', 'UCeLzT-7b2PBcunJplmWtoDg', 'UC_4tXjqecqox5Uc05ncxpxg', 'UCmZA7XRRzmxhM4jPltZX1Zg', 'UCmovZ2th3Sqpd00F5RdeigQ', 'UCLhUvJ_wO9hOvv_yYENu4fQ', 'UCLO9QDxVL4bnvRRsz6K4bsQ', 'UCt5-0i4AVHXaWJrL8Wql3mw', 'UC727SQYUvx5pDDGQpTICNWg', 'UCo7TRj3cS-f_1D9ZDmuTsjw', 'UCNW1Ex0r6HsWRD4LCtPwvoQ', 'UCwSOARsvB-Qa6PtuYyK74dA', 'UCdYR5Oyz8Q4g0ZmB4PkTD7g', 'UCmZ1Rbthn-6Jm_qOGjYsh5A', 'UCkIimWZ9gBJRamKF0rmPU8w', 'UCo2N7C-Z91waaR6lF3LL_jw', 'UCuep1JCrMvSxOGgGhBfJuYw', 'UCwokZsOK_uEre70XayaFnzA', 'UCIG9rDtgR45VCZmYnd-4DUw', 'UCIcAj6WkJ8vZ7DeJVgmeqKw', 'UC8C1LLhBhf_E2IBPLSDJXlQ', 'UC5LyYg6cCA4yHEYvtUsir3g', 'UCPvGypSgfDkVe7JG2KygK7A', 'UCjlmCrq4TP1I4xguOtJ-31w', 'UCvUc0m317LWTTPZoBQV479A', 'UCqTGCMjeKOclEEfW8Vs7sXQ']
    # ids=['UCIcAj6WkJ8vZ7DeJVgmeqKw', 'UC5LyYg6cCA4yHEYvtUsir3g', 'UCvUc0m317LWTTPZoBQV479A', 'UCyLGcqYs7RsBb3L0SJfzGYA', 'UCjXBuHmWkieBApgBhDuJMMQ', 'UCurEA8YoqFwimJcAuSHU0MQ', 'UCiMG6VdScBabPhJ1ZtaVmbw', 'UCF_U2GCKHvDz52jWdizppIA', 'UCnvVG9RbOW3J6Ifqo-zKLiw', 'UCuI5XaO-6VkOEhHao6ij7JA', 'UCGWa1dMU_sDCaRQjdabsVgg', 'UCgTzsBI0DIRopMylJEDqnog']
    # for id in ids:
    #     try:
    #         test(f"https://www.youtube.com/channel/{id}")
    #     except Exception as e:
    #         with open("log.txt", 'a',encoding="utf-8") as f:
    #             f.write(f"{id} \n{str(e)}\n")

