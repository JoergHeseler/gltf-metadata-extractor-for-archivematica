# ⚠️ Warning: Experimental Project ⚠️<br><br>glTF Metadata Extractor for Archivematica

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

Valid files should pass characterization with this script and return error code **0**. However, files containing errors should fail characterization and either return error code **1** or **255**.

### Example

If you use this script to characterize the ASCII embedded glTF 2.0 model [`Duck.gltf`](https://github.com/KhronosGroup/glTF-Sample-Models/blob/main/2.0/Duck/glTF-Embedded/Duck.gltf), the error code **0** should be returned and the following XML content will be included in the AIP's METS document in the <objectCharacteristicsExtension> element of the file:

```xml
<?xml version="1.0" ?>
<GLTFMetadataExtractor>
    <formatName>GLTF</formatName>
    <formatVersion>2.0</formatVersion>
    <size>162796</size>
    <SHA256Checksum>b69c34f30ec2803a37c6546c890a202f4db618745a3fefa3e5ac360bff211931</SHA256Checksum>
    <creationDate>2024-10-26T14:34:56.998537</creationDate>
    <modificationDate>2023-05-31T10:26:56</modificationDate>
    <generator>COLLADA2GLTF</generator>
    <hasDefaultScene>True</hasDefaultScene>
    <totalVertexCount>2399</totalVertexCount>
    <totalTriangleCount>4212</totalTriangleCount>
    <materialCount>1</materialCount>
    <hasTextures>True</hasTextures>
    <animationCount>0</animationCount>
    <hasSkins>False</hasSkins>
    <rawGLTFValidatorOutput>{
    &quot;uri&quot;: &quot;var/archivematica/sharedDirectory/watchedDirectories/workFlowDecisions/extractPackagesChoice/g14_3-5d2becc4-fd78-42a4-accb-a6a8382efd79/objects/Duck.gltf&quot;,
    &quot;mimeType&quot;: &quot;model/gltf+json&quot;,
    &quot;validatorVersion&quot;: &quot;2.0.0-dev.3.8&quot;,
    &quot;issues&quot;: {
        &quot;numErrors&quot;: 0,
        &quot;numWarnings&quot;: 0,
        &quot;numInfos&quot;: 0,
        &quot;numHints&quot;: 0,
        &quot;messages&quot;: [],
        &quot;truncated&quot;: false
    },
    &quot;info&quot;: {
        &quot;version&quot;: &quot;2.0&quot;,
        &quot;generator&quot;: &quot;COLLADA2GLTF&quot;,
        &quot;resources&quot;: [
            {
                &quot;pointer&quot;: &quot;/buffers/0&quot;,
                &quot;mimeType&quot;: &quot;application/gltf-buffer&quot;,
                &quot;storage&quot;: &quot;data-uri&quot;,
                &quot;byteLength&quot;: 102040
            },
            {
                &quot;pointer&quot;: &quot;/images/0&quot;,
                &quot;mimeType&quot;: &quot;image/png&quot;,
                &quot;storage&quot;: &quot;data-uri&quot;,
                &quot;image&quot;: {
                    &quot;width&quot;: 512,
                    &quot;height&quot;: 512,
                    &quot;format&quot;: &quot;rgb&quot;,
                    &quot;primaries&quot;: &quot;srgb&quot;,
                    &quot;transfer&quot;: &quot;srgb&quot;,
                    &quot;bits&quot;: 8
                }
            }
        ],
        &quot;animationCount&quot;: 0,
        &quot;materialCount&quot;: 1,
        &quot;hasMorphTargets&quot;: false,
        &quot;hasSkins&quot;: false,
        &quot;hasTextures&quot;: true,
        &quot;hasDefaultScene&quot;: true,
        &quot;drawCallCount&quot;: 1,
        &quot;totalVertexCount&quot;: 2399,
        &quot;totalTriangleCount&quot;: 4212,
        &quot;maxUVs&quot;: 1,
        &quot;maxInfluences&quot;: 0,
        &quot;maxAttributes&quot;: 3
    }
}</rawGLTFValidatorOutput>
</GLTFMetadataExtractor>
```

## Discussion / Open Questions

1. What **output formats** should be used here? Just pure XML, PREMIS or something else?
2. Is it necessary to output **technical metadata like file size, checksum, creation date etc.**?
3. What **minimal 3D data** should be captured for all 3D formats?
4. Should a **fixed vocabulary be used** for 3D? If so, should a new schema for metadata be created to extract technical 3D metadata? As far as I know, there are currently only IFCm, E57m and BUILDm.
5. Is the **official glTF validator suitable** for metadata extraction or should instead separate source code for each sub-format be written? The advantage of the official version is that it evaluates all versions regardless of whether ASCII or binary and returns common technical metadata. A custom development would be more complex and focus on a specific subversion.

## Dependencies

[Archivematica 1.13.2](https://github.com/artefactual/archivematica/releases/tag/v1.13.2) and [glTF-Validator 2.0.0-dev.3.8](https://github.com/KhronosGroup/glTF-Validator/releases/tag/2.0.0-dev.3.8) were used to analyze, design, develop and test this script.

## Background

As part of the [NFDI4Culture](https://nfdi4culture.de/) initiative, efforts are underway to enhance the capabilities of open-source digital preservation software like Archivematica to identify, validate and characterize 3D file formats. This repository provides a script to improve metadata extraction of Graphics Language Transmission Format (glTF) files in Archivematica, enhancing its 3D content preservation capabilities.

## Related projects

- [3D Sample Files for Digital Preservation Testing](https://github.com/JoergHeseler/3d-sample-files-for-digital-preservation-testing)
- [DAE Validator for Archivematica](https://github.com/JoergHeseler/dae-validator-for-archivematica)
- [glTF Validator for Archivematica](https://github.com/JoergHeseler/gltf-validator-for-archivematica)
- [Siegfried Falls Back on Fido Identifier for Archivematica](https://github.com/JoergHeseler/siegfried-falls-back-on-fido-identifier-for-archivematica)
- [STL Validator for Archivematica](https://github.com/JoergHeseler/stl-validator-for-archivematica)
- [X3D Validator for Archivematica](https://github.com/JoergHeseler/x3d-validator-for-archivematica)

## Imprint

[NFDI4Culture](https://nfdi4culture.de/) – Consortium for Research Data on Material and Immaterial Cultural Heritage

NFDI4Culture is a consortium within the German [National Research Data Infrastructure (NFDI)](https://www.nfdi.de/).

Author: [Jörg Heseler](https://orcid.org/0000-0002-1497-627X)

This project is licensed under a [Creative Commons Attribution 4.0 International License (CC BY 4.0)](https://creativecommons.org/licenses/by/4.0/).

NFDI4Culture is funded by the German Research Foundation (DFG) – Project number – [441958017](https://gepris.dfg.de/gepris/projekt/441958017).
