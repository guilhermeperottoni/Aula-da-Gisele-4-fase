PGDMP     $                
    x            prova    13.0    13.0 
    �           0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                      false            �           0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                      false            �           0    0 
   SEARCHPATH 
   SEARCHPATH     8   SELECT pg_catalog.set_config('search_path', '', false);
                      false            �           1262    24576    prova    DATABASE     e   CREATE DATABASE prova WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE = 'Portuguese_Brazil.1252';
    DROP DATABASE prova;
                postgres    false            �            1259    24579    musica    TABLE     �   CREATE TABLE public.musica (
    id integer NOT NULL,
    nome character varying(255),
    autor character varying(255),
    genero character varying(255)
);
    DROP TABLE public.musica;
       public         heap    postgres    false            �            1259    24577    musica_id_seq    SEQUENCE     �   CREATE SEQUENCE public.musica_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 $   DROP SEQUENCE public.musica_id_seq;
       public          postgres    false    201            �           0    0    musica_id_seq    SEQUENCE OWNED BY     ?   ALTER SEQUENCE public.musica_id_seq OWNED BY public.musica.id;
          public          postgres    false    200            #           2604    24582 	   musica id    DEFAULT     f   ALTER TABLE ONLY public.musica ALTER COLUMN id SET DEFAULT nextval('public.musica_id_seq'::regclass);
 8   ALTER TABLE public.musica ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    200    201    201            �          0    24579    musica 
   TABLE DATA           9   COPY public.musica (id, nome, autor, genero) FROM stdin;
    public          postgres    false    201   2	       �           0    0    musica_id_seq    SEQUENCE SET     ;   SELECT pg_catalog.setval('public.musica_id_seq', 2, true);
          public          postgres    false    200            �   V   x�3�tNLKUHUH��/�t/-.I,�W���MT�N-*I�K��W�2�tI--V8�R� �H!����bN�d��Ģ�bN�Ҽl�=... �g�     