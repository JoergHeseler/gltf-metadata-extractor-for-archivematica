# glTF Metadata Extractor for Archivematica [Work in Progress]

This repository provides a script that uses the official [glTF-Validator](https://github.com/KhronosGroup/glTF-Validator/releases) tool to extract metadata from Graphics Language Transmission Format (glTF) files in [Archivematica](https://www.archivematica.org/).

## Installation

To install this script, follow these steps:

If you have already installed the official glTF validator tool in Archivematica, you can skip steps 1 and 2.

### 1. Download the official glTF-Validator tool

- Download the latest release of the [glTF-Validator](https://github.com/KhronosGroup/glTF-Validator/releases) and install it in the `/usr/share/` folder.

### 2. Create a new format policy tool

- In the Archivematica frontend, navigate to **Preservation planning** > **Format policy registry** > **Tools** > **Create new tool** or go directly to [this link](http://10.10.10.20/fpr/fptool/create/).
- Enter the following parameters:
  - **Description**: Enter `gltf_validator`.
  - **Version**: Enter the version you downloaded, e. g. `2.0.0-dev.3.8`.
- Click **Save**.

### 3. Create a new characterization command

- In the Archivematica frontend, navigate to **Preservation planning** > **Characterization** > **Commands** > **Create new command** or go directly to [this link](http://10.10.10.20/fpr/fpcommand/create/).
- Fill in the following fields:
  - **The related tool**: Select **gltf_validator**.
  - **Description**: Enter `Characterize using gltf_validator`.
  - **Command**: Paste the entire content of the [**gltf-metadata-extractor.py**](./src/gltf-metadata-extractor.py) file.
  - **Script type**: Select **Python script**.
  - **Command usage**: Select **Characterization**.
  - Leave all other input fields and combo boxes untouched.
- Click **Save**.

### 4. Create a new validation rule for ASCII based glTF 1.0

- In the Archivematica frontend, navigate to **Preservation planning** > **Characterization** > **Rules** > **Create new rule** or go directly to [this link](http://10.10.10.20/fpr/fprule/create/).
- Fill in the following fields:
  - **Purpose**: Select **Characterization**.
  - **The related format**: Select **Model: GL Transmission Format (Text): GLTF 1.0 (fmt/1314)**.
  - **Command**: Select **Characterize using gltf_validator**.
- Click **Save**.

### 5. Create a new validation rule for ASCII based glTF 2.0

- In the Archivematica frontend, navigate to **Preservation planning** > **Characterization** > **Rules** > **Create new rule** or go directly to [this link](http://10.10.10.20/fpr/fprule/create/).
- Fill in the following fields:
  - **Purpose**: Select **Characterization**.
  - **The related format**: Select **Model: GL Transmission Format (Text): GLTF 2.0 (fmt/1315)**.
  - **Command**: Select **Characterize using gltf_validator**.
- Click **Save**.

### 6. Create a new validation rule for binary glTF files

- In the Archivematica frontend, navigate to **Preservation planning** > **Characterization** > **Rules** > **Create new rule** or go directly to [this link](http://10.10.10.20/fpr/fprule/create/).
- Fill in the following fields:
  - **Purpose**: Select **Characterization**.
  - **The related format**: Select **Model: GL Transmission Format (Binary): GLTF (Binary) (fmt/1316)**.
  - **Command**: Select **Characterize using gltf_validator**.
- Click **Save**.

## Test

To test this metadata exctractor, you can use the sample glTF files located [here](https://github.com/JoergHeseler/3d-sample-files-for-digital-preservation-testing/tree/main/gltf).

You can view the error codes and detailed characterization results in the Archivmatica frontend after starting a transfer by expanding the `▸ Microservice: Characterize and extract metadata` section and clicking on the gear icon of `Microservice: Characterize and extract metadata`.

Files with no errors end with `valid` in their name and should pass characterization with this script (i. e. return error code **0**). However, all other files contain errors and should fail characterization (i. e. return error code **1** or **255**).

## Dependencies

[Archivematica 1.13.2](https://github.com/artefactual/archivematica/releases/tag/v1.13.2) and [glTF-Validator 2.0.0-dev.3.8](https://github.com/KhronosGroup/glTF-Validator/releases/tag/2.0.0-dev.3.8) were used to analyze, design, develop and test this script.

## Background

As part of the [NFDI4Culture](https://nfdi4culture.de/) initiative, efforts are underway to enhance the capabilities of open-source digital preservation software like Archivematica to identify, validate and characterize 3D file formats. This repository provides a script to improve metadata extraction of Graphics Language Transmission Format (glTF) files in Archivematica, enhancing its 3D content preservation capabilities.

## Related projects

- [3D Sample Files for Digital Preservation Testing](https://github.com/JoergHeseler/3d-sample-files-for-digital-preservation-testing)
- [DAE Validator for Archivematica](https://github.com/JoergHeseler/dae-validator-for-archivematica)
- [Siegfried Falls Back on Fido Identifier for Archivematica](https://github.com/JoergHeseler/siegfried-falls-back-on-fido-identifier-for-archivematica)
- [STL Validator for Archivematica](https://github.com/JoergHeseler/stl-validator-for-archivematica)
- [X3D Validator for Archivematica](https://github.com/JoergHeseler/x3d-validator-for-archivematica)

## Imprint

[NFDI4Culture](https://nfdi4culture.de/) – Consortium for Research Data on Material and Immaterial Cultural Heritage

NFDI4Culture is a consortium within the German [National Research Data Infrastructure (NFDI)](https://www.nfdi.de/).

Author: [Jörg Heseler](https://orcid.org/0000-0002-1497-627X)

This project is licensed under a [Creative Commons Attribution 4.0 International License (CC BY 4.0)](https://creativecommons.org/licenses/by/4.0/).

NFDI4Culture is funded by the German Research Foundation (DFG) – Project number – [441958017](https://gepris.dfg.de/gepris/projekt/441958017).