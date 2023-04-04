# WCA

## Programa que permite analizar la conversación de whatsapp.

El archivo de entrada debe llamarse chat.txt, este debe de exportarlo desde el chat que quiere analizar. 


### Front-End Performance ###

As of version 2.0.0, _Subtitles_ outputs its CSS via `wp_head`. This is to load sensible CSS that will ensure your subtitle is always scaled properly alongside your website title and never shown in comment areas.

```css
/**
 * Plugin Name: Subtitles
 * Plugin URI: http://wordpress.org/plugins/subtitles/
 * Description: Easily add subtitles into your WordPress posts, pages, custom post types, and themes.
 * Author: We Cobble
 * Author URI: https://wecobble.com/
 * Version: 2.1.1
 * License: GNU General Public License v2 or later
 * License URI: http://www.gnu.org/licenses/gpl-2.0.html
 */

/**
 * Be explicit about this styling only applying to spans,
 * since that's the default markup that's returned by
 * Subtitles. If a developer overrides the default subtitles
 * markup with another element or class, we don't want to stomp
 * on that.
 *
 * @since 1.0.0
 */
span.entry-subtitle {
	display: block; /* Put subtitles on their own line by default. */
	font-size: 0.53333333333333em; /* Sensible scaling. It's assumed that post titles will be wrapped in heading tags. */
}
/**
 * If subtitles are shown in comment areas, we'll hide them by default.
 *
 * @since 1.0.5
 */
#comments .comments-title span.entry-subtitle {
	display: none;
}
```


Las graficas que genera este programa son: 

## Mensajes enviados por cada usuario

![!mensajes_enviados_por usuario](https://github.com/PeterArguetaYT/WCA-Android/raw/main/01_msj_enviados_usuario.png)


## Mapa de palabras


![!Mapa_palabra](https://github.com/PeterArguetaYT/WCA-Android/raw/main/02_mapa_palabra.png)



## Mensajes enviados por semana

![!msj_enviados_por_semana](https://github.com/PeterArguetaYT/WCA-Android/raw/main/03_msj_enviados_por_semana.png)

## Hora de los mensajes

![!hora_de_los_mensajes](https://github.com/PeterArguetaYT/WCA-Android/raw/main/04_hora_de_los_msj.png)

## Multimedia enviada


![!multimedia](https://github.com/PeterArguetaYT/WCA-Android/raw/main/05_multimedia.png)


## Promedio de mensajes diarios

![!msj_diarios](https://github.com/PeterArguetaYT/WCA-Android/raw/main/06_promedio_msj_diarios.png)

