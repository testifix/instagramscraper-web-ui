o
    ;�bl	  �                   @   s�   U d dl mZ d dlT d dlZd dlZd dlZe�eejd �	dd��	dd��	d	d
��	dd���Z
e
d Ze
d Ze
d Zeed< e
d Zeed< eee
d ��Zeed< e
d Zeed< G dd� d�Zedkrxee�Zeed< e�ee� dS dS )�    )�Client)�*N�   �,z","�:z":"�}z"}�{z{"Z	loginNameZ	loginPass�orderId�
SIPARIS_IDZtargetAccount�HEDEF_HESAPZ	postLimit�LIMITZserviceName�HIZMETc                   @   sN   e Zd Zddd�dededefdd�Zd	ed
efdd�Zdedefdd�ZdS )�InstagramPostScraperZpostsz{0}.txt)�
foldername�filenamer	   r   r   c                G   sP   t �t j�|�sd|� �nd� || _|d |�|� | _t| jddd�| _d S )Nzmkdir � �/zw+zutf-8)�encoding)	�os�system�path�existsr	   �format�absPath�open�file)�selfr	   r   r   �args� r   ��F:\WindowsDirectories\Backup\a1_0\Documents\Bionluk.com\canercakmak16\InstagramPostScraper-WebSocket-Interactive\simple-websocket-server-client\server\module.py�__init__   s    zInstagramPostScraper.__init__�content�returnc                 C   s    z	| j �|� W dS    Y dS )NFT)r   �write)r   r!   r   r   r   r#      s
   �zInstagramPostScraper.write�username�limitc                 C   s�   |dk s|dkrt d� t� }|�tt� |j|�|�|d�}|D ]}| jd |j d t	 d }| �
|�r7q!q!td| j� d	�� d S )
Nr   i�  z"Limit ayari 0-500 arasi olmalidir!)�amountz|https://instagram.com/p/�|�
zVeriler yazdirildi! Konum: z
statusCODE=success)�exitr   Zlogin�GIRIS_YAPILACAK_KULLANICI�GIRIS_YAPILACAK_KULLANICI_SIFREZuser_mediasZuser_id_from_usernamer	   �coder   r#   �printr   )r   r$   r%   ZclientZmediasZmediaZdataToWriter   r   r   �getPosts%   s   
�zInstagramPostScraper.getPostsN)	�__name__�
__module__�__qualname__�strr    �boolr#   �intr.   r   r   r   r   r      s    r   �__main__�scraper)Z
instagrapir   Zinstagrapi.exceptionsr   �sysZjson�loads�eval�argv�replace�paramsr*   r+   r
   r2   �__annotations__r   r4   r   r   r   r/   r6   r.   r   r   r   r   �<module>   s    4	�