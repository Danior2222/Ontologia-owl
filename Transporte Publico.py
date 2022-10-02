<?xml version="1.0"?>


<!DOCTYPE Ontology [
    <!ENTITY xsd "http://www.w3.org/2001/XMLSchema#" >
    <!ENTITY xml "http://www.w3.org/XML/1998/namespace" >
    <!ENTITY rdfs "http://www.w3.org/2000/01/rdf-schema#" >
    <!ENTITY rdf "http://www.w3.org/1999/02/22-rdf-syntax-ns#" >
]>


<Ontology xmlns="http://www.w3.org/2002/07/owl#"
     xml:base="http://www.semanticweb.org/samsung/ontologies/2016/0/untitled-ontology-12"
     xmlns:rdfs="http://www.w3.org/2000/01/rdf-schema#"
     xmlns:xsd="http://www.w3.org/2001/XMLSchema#"
     xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"
     xmlns:xml="http://www.w3.org/XML/1998/namespace"
     ontologyIRI="http://www.semanticweb.org/samsung/ontologies/2016/0/untitled-ontology-12">
    <Prefix name="rdf" IRI="http://www.w3.org/1999/02/22-rdf-syntax-ns#"/>
    <Prefix name="rdfs" IRI="http://www.w3.org/2000/01/rdf-schema#"/>
    <Prefix name="xsd" IRI="http://www.w3.org/2001/XMLSchema#"/>
    <Prefix name="owl" IRI="http://www.w3.org/2002/07/owl#"/>
    <Annotation>
        <AnnotationProperty IRI="http://purl.org/dc/terms/creator"/>
        <Literal datatypeIRI="&rdf;PlainLiteral">Daniel Orlando Garzon Pinzon</Literal>
    </Annotation>
    <Declaration>
        <Class IRI="#Bus"/>
    </Declaration>
    <Declaration>
        <Class IRI="#Parada"/>
    </Declaration>
    <Declaration>
        <Class IRI="#Parada_autobús"/>
    </Declaration>
    <Declaration>
        <Class IRI="#Vehículo_transporte"/>
    </Declaration>
    <Declaration>
        <Class IRI="#horario"/>
    </Declaration>
    <Declaration>
        <Class IRI="#costo"/>
    </Declaration>
    <Declaration>
        <Class IRI="#horario"/>
    </Declaration>
    <Declaration>
        <ObjectProperty IRI="#autobús_de_transporte"/>
    </Declaration>
    <Declaration>
        <ObjectProperty IRI="#parada_destino"/>
    </Declaration>
    <Declaration>
        <ObjectProperty IRI="#parada_origen"/>
    </Declaration>
    <Declaration>
        <ObjectProperty IRI="#tiene_horario"/>
    </Declaration>
    <Declaration>
        <ObjectProperty IRI="#tiene_paradas_intermedias"/>
    </Declaration>
    <Declaration>
        <ObjectProperty IRI="#tiene_costo"/>
    </Declaration>
    <Declaration>
        <ObjectProperty IRI="#tiene_tramo_horario"/>
    </Declaration>
    <Declaration>
        <DataProperty IRI="#Codigo_Parada"/>
    </Declaration>
    <Declaration>
        <DataProperty IRI="#Ubicación"/>
    </Declaration>
    <Declaration>
        <DataProperty IRI="#aforo_máximo"/>
    </Declaration>
    <Declaration>
        <DataProperty IRI="#coste_unitario"/>
    </Declaration>
    <Declaration>
        <DataProperty IRI="#descriptor_parada"/>
    </Declaration>
    <Declaration>
        <DataProperty IRI="#fin_tramo_horario"/>
    </Declaration>
    <Declaration>
        <DataProperty IRI="#frecuencia_de_servicio"/>
    </Declaration>
    <Declaration>
        <DataProperty IRI="#hora_apertura_parada"/>
    </Declaration>
    <Declaration>
        <DataProperty IRI="#hora_de_cierre_parada"/>
    </Declaration>
    <Declaration>
        <DataProperty IRI="#hora_de_inicio"/>
    </Declaration>
    <Declaration>
        <DataProperty IRI="#hora_fin"/>
    </Declaration>
    <Declaration>
        <DataProperty IRI="#horario_festivo"/>
    </Declaration>
    <Declaration>
        <DataProperty IRI="#inicio_tamo_horario"/>
    </Declaration>
    <Declaration>
        <DataProperty IRI="#parada_ida"/>
    </Declaration>
    <Declaration>
        <DataProperty IRI="#pertenece_a_estacion"/>
    </Declaration>
    <Declaration>
        <NamedIndividual IRI="#PORTAL_NORTE"/>
    </Declaration>
    <Declaration>
        <NamedIndividual IRI="#CAllE_100"/>
    </Declaration>
    <Declaration>
        <NamedIndividual IRI="#EMT"/>
    </Declaration>
    <Declaration>
        <NamedIndividual IRI="#PORTAL_SUR"/>
    </Declaration>
    <Declaration>
        <NamedIndividual IRI="#VOLVO"/>
    </Declaration>
    <Declaration>
        <NamedIndividual IRI="#CALLE_75"/>
    </Declaration>
    <Declaration>
        <NamedIndividual IRI="#CASTELLANA"/>
    </Declaration>
    <Declaration>
        <NamedIndividual IRI="#RICAURTE"/>
    </Declaration>
    <Declaration>
        <NamedIndividual IRI="#horario_festivo"/>
    </Declaration>
    <Declaration>
        <NamedIndividual IRI="#horario_laboral"/>
    </Declaration>
    <Declaration>
        <NamedIndividual IRI="#tramo_horario_mañana"/>
    </Declaration>
    <Declaration>
        <NamedIndividual IRI="#tramo_horario_tarde_festivo"/>
    </Declaration>
    <Declaration>
        <NamedIndividual IRI="#tramo_tarde_normal"/>
    </Declaration>
    <SubClassOf>
        <Class IRI="#Bus"/>
        <Class IRI="#Vehículo_transporte"/>
    </SubClassOf>
    <SubClassOf>
        <Class IRI="#Parada_autobús"/>
        <Class IRI="#Parada"/>
    </SubClassOf>
    <ObjectPropertyAssertion>
        <ObjectProperty IRI="#tiene_tramo_horario"/>
        <NamedIndividual IRI="#horario_festivo"/>
        <NamedIndividual IRI="#tramo_horario_tarde_festivo"/>
    </ObjectPropertyAssertion>
    <ObjectPropertyAssertion>
        <ObjectProperty IRI="#tiene_tramo_horario"/>
        <NamedIndividual IRI="#horario_festivo"/>
        <NamedIndividual IRI="#tramo_horario_mañana"/>
    </ObjectPropertyAssertion>
    <ObjectPropertyAssertion>
        <ObjectProperty IRI="#tiene_tramo_horario"/>
        <NamedIndividual IRI="#horario_laboral"/>
        <NamedIndividual IRI="#tramo_tarde_normal"/>
    </ObjectPropertyAssertion>
    <ObjectPropertyAssertion>
        <ObjectProperty IRI="#tiene_tramo_horario"/>
        <NamedIndividual IRI="#horario_laboral"/>
        <NamedIndividual IRI="#tramo_horario_mañana"/>
    </ObjectPropertyAssertion>
    <ObjectPropertyAssertion>
        <ObjectProperty IRI="#autobús_de_transporte"/>
        <NamedIndividual IRI="#VOLVO"/>
    </ObjectPropertyAssertion>
    <ObjectPropertyAssertion>
        <ObjectProperty IRI="#parada_destino"/>
        <NamedIndividual IRI="#PORTAL_NORTE"/>
    </ObjectPropertyAssertion>
    <ObjectPropertyAssertion>
        <ObjectProperty IRI="#parada_origen"/>
        <NamedIndividual IRI="#PORTAL_SUR"/>
    </ObjectPropertyAssertion>
    <ObjectPropertyAssertion>
        <ObjectProperty IRI="#tiene_horario"/>
        <NamedIndividual IRI="#horario_festivo"/>
    </ObjectPropertyAssertion>
    <ObjectPropertyAssertion>
        <ObjectProperty IRI="#tiene_horario"/>
        <NamedIndividual IRI="#horario_laboral"/>
    </ObjectPropertyAssertion>
    <ObjectPropertyAssertion>
        <ObjectProperty IRI="#tiene_paradas_intermedias"/>
        <NamedIndividual IRI="#RICAURTE"/>
    </ObjectPropertyAssertion>
    <ObjectPropertyAssertion>
        <ObjectProperty IRI="#tiene_paradas_intermedias"/>
        <NamedIndividual IRI="#CALLE_75"/>
    </ObjectPropertyAssertion>
    <ObjectPropertyAssertion>
        <ObjectProperty IRI="#tiene_paradas_intermedias"/>
        <NamedIndividual IRI="#CASTELLANA"/>
    </ObjectPropertyAssertion>
    <ObjectPropertyAssertion>
        <ObjectProperty IRI="#tiene_paradas_intermedias"/>
        <NamedIndividual IRI="#CAllE_100"/>
    </ObjectPropertyAssertion>
    <ObjectPropertyAssertion>
        <ObjectProperty IRI="#tiene_tarifa"/>
        <NamedIndividual IRI="#tarifa_zona_A"/>
    </ObjectPropertyAssertion>
    <DataPropertyAssertion>
        <DataProperty IRI="#velocidad_máxima_permitida"/>
        <NamedIndividual IRI="#VOLVO"/>
        <Literal datatypeIRI="&xsd;integer">50</Literal>
    </DataPropertyAssertion>
    <DataPropertyAssertion>
        <DataProperty IRI="#dias_aplicables"/>
        <NamedIndividual IRI="#horario_festivo"/>
        <Literal datatypeIRI="&xsd;string">Domingo</Literal>
    </DataPropertyAssertion>
    <DataPropertyAssertion>
        <DataProperty IRI="#dias_aplicables"/>
        <NamedIndividual IRI="#horario_laboral"/>
        <Literal datatypeIRI="&xsd;string">Lunes-Viernes</Literal>
    </DataPropertyAssertion>
    <DataPropertyAssertion>
        <DataProperty IRI="#coste_unitario"/>
        <NamedIndividual IRI="#tarifa_zona_A"/>
        <Literal datatypeIRI="&rdf;PlainLiteral">1.50</Literal>
    </DataPropertyAssertion>
    <DataPropertyAssertion>
        <DataProperty IRI="#zona_tarifaria"/>
        <NamedIndividual IRI="#tarifa_zona_A"/>
        <Literal datatypeIRI="&rdf;PlainLiteral">A</Literal>
    </DataPropertyAssertion>
    <DataPropertyAssertion>
        <DataProperty IRI="#fin_tramo_horario"/>
        <NamedIndividual IRI="#tramo_horario_mañana"/>
        <Literal datatypeIRI="&xsd;string">12:00</Literal>
    </DataPropertyAssertion>
    <DataPropertyAssertion>
        <DataProperty IRI="#fin_tramo_horario"/>
        <NamedIndividual IRI="#tramo_horario_mañana"/>
        <Literal datatypeIRI="&xsd;string"></Literal>
    </DataPropertyAssertion>
    <DataPropertyAssertion>
        <DataProperty IRI="#frecuencia_de_servicio"/>
        <NamedIndividual IRI="#tramo_horario_mañana"/>
        <Literal datatypeIRI="&xsd;integer">10</Literal>
    </DataPropertyAssertion>
    <DataPropertyAssertion>
        <DataProperty IRI="#inicio_tamo_horario"/>
        <NamedIndividual IRI="#tramo_horario_mañana"/>
        <Literal datatypeIRI="&xsd;string">6:00</Literal>
    </DataPropertyAssertion>
    <DataPropertyAssertion>
        <DataProperty IRI="#fin_tramo_horario"/>
        <NamedIndividual IRI="#tramo_horario_tarde_festivo"/>
        <Literal datatypeIRI="&xsd;string">23:30</Literal>
    </DataPropertyAssertion>
    <DataPropertyAssertion>
        <DataProperty IRI="#frecuencia_de_servicio"/>
        <NamedIndividual IRI="#tramo_horario_tarde_festivo"/>
        <Literal datatypeIRI="&xsd;integer">15</Literal>
    </DataPropertyAssertion>
    <DataPropertyAssertion>
        <DataProperty IRI="#inicio_tamo_horario"/>
        <NamedIndividual IRI="#tramo_horario_tarde_festivo"/>
        <Literal datatypeIRI="&xsd;string">12:00</Literal>
    </DataPropertyAssertion>
    <DataPropertyAssertion>
        <DataProperty IRI="#fin_tramo_horario"/>
        <NamedIndividual IRI="#tramo_tarde_normal"/>
        <Literal datatypeIRI="&xsd;string">23:30</Literal>
    </DataPropertyAssertion>
    <DataPropertyAssertion>
        <DataProperty IRI="#frecuencia_de_servicio"/>
        <NamedIndividual IRI="#tramo_tarde_normal"/>
        <Literal datatypeIRI="&xsd;integer">7</Literal>
    </DataPropertyAssertion>
    <DataPropertyAssertion>
        <DataProperty IRI="#inicio_tamo_horario"/>
        <NamedIndividual IRI="#tramo_tarde_normal"/>
        <Literal datatypeIRI="&xsd;string">12:00</Literal>
    </DataPropertyAssertion>
    <SubObjectPropertyOf>
        <ObjectProperty IRI="#parada_destino"/>
        <ObjectProperty abbreviatedIRI="owl:topObjectProperty"/>
    </SubObjectPropertyOf>
    <SubObjectPropertyOf>
        <ObjectProperty IRI="#tiene_tramo_horario"/>
        <ObjectProperty abbreviatedIRI="owl:topObjectProperty"/>
    </SubObjectPropertyOf>
    <ObjectPropertyDomain>
        <ObjectProperty IRI="#autobús_de_transporte"/>
    </ObjectPropertyDomain>
    <ObjectPropertyDomain>
        <ObjectProperty IRI="#parada_destino"/>
    </ObjectPropertyDomain>
    <ObjectPropertyDomain>
        <ObjectProperty IRI="#parada_origen"/>
    </ObjectPropertyDomain>
    <ObjectPropertyDomain>
        <ObjectProperty IRI="#tiene_horario"/>
    </ObjectPropertyDomain>
    <ObjectPropertyDomain>
        <ObjectProperty IRI="#tiene_paradas_intermedias"/>
    </ObjectPropertyDomain>
    <ObjectPropertyDomain>
        <ObjectProperty IRI="#tiene_tarifa"/>
    </ObjectPropertyDomain>
    <ObjectPropertyDomain>
        <ObjectProperty IRI="#tiene_tramo_horario"/>
        <Class IRI="#horario"/>
    </ObjectPropertyDomain>
    <ObjectPropertyRange>
        <ObjectProperty IRI="#autobús_de_transporte"/>
        <Class IRI="#Bus"/>
    </ObjectPropertyRange>
    <ObjectPropertyRange>
        <ObjectProperty IRI="#parada_destino"/>
        <Class IRI="#Parada"/>
    </ObjectPropertyRange>
    <ObjectPropertyRange>
        <ObjectProperty IRI="#parada_origen"/>
        <Class IRI="#Parada"/>
    </ObjectPropertyRange>
    <ObjectPropertyRange>
        <ObjectProperty IRI="#tiene_horario"/>
        <Class IRI="#horario"/>
    </ObjectPropertyRange>
    <ObjectPropertyRange>
        <ObjectProperty IRI="#tiene_paradas_intermedias"/>
        <Class IRI="#Parada"/>
    </ObjectPropertyRange>
    <ObjectPropertyRange>
        <ObjectProperty IRI="#tiene_tarifa"/>
        <Class IRI="#tarifa"/>
    </ObjectPropertyRange>
    <ObjectPropertyRange>
        <ObjectProperty IRI="#tiene_tramo_horario"/>
        <Class IRI="#tramo_horario"/>
    </ObjectPropertyRange>
    <SubDataPropertyOf>
        <DataProperty IRI="#aforo_máximo"/>
        <DataProperty abbreviatedIRI="owl:topDataProperty"/>
    </SubDataPropertyOf>
    <SubDataPropertyOf>
        <DataProperty IRI="#coste_abono_mensual"/>
        <DataProperty abbreviatedIRI="owl:topDataProperty"/>
    </SubDataPropertyOf>
    <SubDataPropertyOf>
        <DataProperty IRI="#coste_unitario"/>
        <DataProperty abbreviatedIRI="owl:topDataProperty"/>
    </SubDataPropertyOf>
    <SubDataPropertyOf>
        <DataProperty IRI="#fin_tramo_horario"/>
        <DataProperty abbreviatedIRI="owl:topDataProperty"/>
    </SubDataPropertyOf>
    <SubDataPropertyOf>
        <DataProperty IRI="#frecuencia_de_servicio"/>
        <DataProperty abbreviatedIRI="owl:topDataProperty"/>
    </SubDataPropertyOf>
    <SubDataPropertyOf>
        <DataProperty IRI="#hora_apertura_parada"/>
        <DataProperty abbreviatedIRI="owl:topDataProperty"/>
    </SubDataPropertyOf>
    <SubDataPropertyOf>
        <DataProperty IRI="#hora_de_cierre_parada"/>
        <DataProperty abbreviatedIRI="owl:topDataProperty"/>
    </SubDataPropertyOf>
    <SubDataPropertyOf>
        <DataProperty IRI="#hora_de_inicio"/>
        <DataProperty abbreviatedIRI="owl:topDataProperty"/>
    </SubDataPropertyOf>
    <SubDataPropertyOf>
        <DataProperty IRI="#horario_festivo"/>
        <DataProperty abbreviatedIRI="owl:topDataProperty"/>
    </SubDataPropertyOf>
    <SubDataPropertyOf>
        <DataProperty IRI="#página_web_agencia"/>
        <DataProperty abbreviatedIRI="owl:topDataProperty"/>
    </SubDataPropertyOf>
    <SubDataPropertyOf>
        <DataProperty IRI="#telefóno_contacto_agencia"/>
        <DataProperty abbreviatedIRI="owl:topDataProperty"/>
    </SubDataPropertyOf>
    <SubDataPropertyOf>
        <DataProperty IRI="#velocidad_máxima_permitida"/>
        <DataProperty abbreviatedIRI="owl:topDataProperty"/>
    </SubDataPropertyOf>
    <SubDataPropertyOf>
        <DataProperty IRI="#zona_tarifaria"/>
        <DataProperty abbreviatedIRI="owl:topDataProperty"/>
    </SubDataPropertyOf>
    <DataPropertyDomain>
        <DataProperty IRI="#Codigo_Parada"/>
        <Class IRI="#Parada"/>
    </DataPropertyDomain>
    <DataPropertyDomain>
        <DataProperty IRI="#Ubicación"/>
        <Class IRI="#Parada"/>
    </DataPropertyDomain>
    <DataPropertyDomain>
        <DataProperty IRI="#aforo_máximo"/>
        <Class IRI="#Vehículo_transporte"/>
    </DataPropertyDomain>
    <DataPropertyDomain>
        <DataProperty IRI="#coste_abono_mensual"/>
        <Class IRI="#tarifa"/>
    </DataPropertyDomain>
    <DataPropertyDomain>
        <DataProperty IRI="#coste_unitario"/>
        <Class IRI="#tarifa"/>
    </DataPropertyDomain>
    <DataPropertyDomain>
        <DataProperty IRI="#descriptor_parada"/>
        <Class IRI="#Parada"/>
    </DataPropertyDomain>
    <DataPropertyDomain>
        <DataProperty IRI="#dias_aplicables"/>
        <Class IRI="#horario"/>
    </DataPropertyDomain>
    <DataPropertyDomain>
        <DataProperty IRI="#fin_tramo_horario"/>
        <Class IRI="#tramo_horario"/>
    </DataPropertyDomain>
    <DataPropertyDomain>
        <DataProperty IRI="#frecuencia_de_servicio"/>
        <Class IRI="#tramo_horario"/>
    </DataPropertyDomain>
    <DataPropertyDomain>
        <DataProperty IRI="#hora_apertura_parada"/>
        <Class IRI="#Parada_metro"/>
    </DataPropertyDomain>
    <DataPropertyDomain>
        <DataProperty IRI="#hora_de_cierre_parada"/>
        <Class IRI="#Parada_metro"/>
    </DataPropertyDomain>
    <DataPropertyDomain>
        <DataProperty IRI="#hora_de_inicio"/>
        <Class IRI="#horario"/>
    </DataPropertyDomain>
    <DataPropertyDomain>
        <DataProperty IRI="#hora_fin"/>
        <Class IRI="#horario"/>
    </DataPropertyDomain>
    <DataPropertyDomain>
        <DataProperty IRI="#horario_festivo"/>
        <Class IRI="#horario"/>
    </DataPropertyDomain>
    <DataPropertyDomain>
        <DataProperty IRI="#inicio_tamo_horario"/>
        <Class IRI="#tramo_horario"/>
    </DataPropertyDomain>
    <DataPropertyDomain>
        <DataProperty IRI="#parada_ida"/>
        <Class IRI="#Parada_autobús"/>
    </DataPropertyDomain>
    <DataPropertyDomain>
        <DataProperty IRI="#pertenece_a_estacion"/>
        <Class IRI="#Parada"/>
    </DataPropertyDomain>
    <DataPropertyDomain>
        <DataProperty IRI="#zona_tarifaria"/>
        <Class IRI="#tarifa"/>
    </DataPropertyDomain>
    <DataPropertyRange>
        <DataProperty IRI="#Codigo_Parada"/>
        <Datatype abbreviatedIRI="xsd:integer"/>
    </DataPropertyRange>
    <DataPropertyRange>
        <DataProperty IRI="#Nombre_de_la_agencia"/>
        <Datatype abbreviatedIRI="xsd:string"/>
    </DataPropertyRange>
    <DataPropertyRange>
        <DataProperty IRI="#Ubicación"/>
        <Datatype abbreviatedIRI="xsd:string"/>
    </DataPropertyRange>
    <DataPropertyRange>
        <DataProperty IRI="#aforo_máximo"/>
        <Datatype abbreviatedIRI="xsd:int"/>
    </DataPropertyRange>
    <DataPropertyRange>
        <DataProperty IRI="#coste_unitario"/>
        <Datatype abbreviatedIRI="xsd:double"/>
    </DataPropertyRange>
    <DataPropertyRange>
        <DataProperty IRI="#descriptor_parada"/>
        <Datatype abbreviatedIRI="xsd:string"/>
    </DataPropertyRange>
    <DataPropertyRange>
        <DataProperty IRI="#dias_aplicables"/>
        <Datatype abbreviatedIRI="xsd:string"/>
    </DataPropertyRange>
    <DataPropertyRange>
        <DataProperty IRI="#fin_tramo_horario"/>
        <Datatype abbreviatedIRI="xsd:string"/>
    </DataPropertyRange>
    <DataPropertyRange>
        <DataProperty IRI="#frecuencia_de_servicio"/>
        <Datatype abbreviatedIRI="xsd:int"/>
    </DataPropertyRange>
    <DataPropertyRange>
        <DataProperty IRI="#hora_apertura_parada"/>
        <Datatype abbreviatedIRI="xsd:string"/>
    </DataPropertyRange>
    <DataPropertyRange>
        <DataProperty IRI="#hora_de_cierre_parada"/>
        <Datatype abbreviatedIRI="xsd:string"/>
    </DataPropertyRange>
    <DataPropertyRange>
        <DataProperty IRI="#hora_de_inicio"/>
        <Datatype abbreviatedIRI="xsd:string"/>
    </DataPropertyRange>
    <DataPropertyRange>
        <DataProperty IRI="#hora_fin"/>
        <Datatype abbreviatedIRI="xsd:string"/>
    </DataPropertyRange>
    <DataPropertyRange>
        <DataProperty IRI="#horario_festivo"/>
        <Datatype abbreviatedIRI="xsd:boolean"/>
    </DataPropertyRange>
    <DataPropertyRange>
        <DataProperty IRI="#inicio_tamo_horario"/>
        <Datatype abbreviatedIRI="xsd:string"/>
    </DataPropertyRange>
    <DataPropertyRange>
        <DataProperty IRI="#parada_ida"/>
        <Datatype abbreviatedIRI="xsd:boolean"/>
    </DataPropertyRange>
    <DataPropertyRange>
        <DataProperty IRI="#pertenece_a_estacion"/>
        <Datatype abbreviatedIRI="xsd:boolean"/>
    </DataPropertyRange>
    <DataPropertyRange>
        <DataProperty IRI="#velocidad_máxima_permitida"/>
        <Datatype abbreviatedIRI="xsd:int"/>
    </DataPropertyRange>
    <DataPropertyRange>
        <DataProperty IRI="#zona_tarifaria"/>
        <Datatype abbreviatedIRI="xsd:string"/>
    </DataPropertyRange>
    </AnnotationAssertion>
    <AnnotationAssertion>
        <AnnotationProperty abbreviatedIRI="rdfs:comment"/>
        <IRI>#Ubicación</IRI>
        <Literal datatypeIRI="&rdf;PlainLiteral">Ubicación en coordenadas de la parada</Literal>
    </AnnotationAssertion>
    <AnnotationAssertion>
        <AnnotationProperty abbreviatedIRI="rdfs:comment"/>
        <IRI>#aforo_máximo</IRI>
        <Literal datatypeIRI="&rdf;PlainLiteral">Número de pasajeros máximo del medio de transporte
    </Literal>
    </AnnotationAssertion>
    <AnnotationAssertion>
        <AnnotationProperty abbreviatedIRI="rdfs:comment"/>
        <IRI>#autobús_de_transporte</IRI>
        <Literal datatypeIRI="&rdf;PlainLiteral">Transporte que presta servicio en la línea</Literal>
    </AnnotationAssertion>
    <AnnotationAssertion>
        <AnnotationProperty abbreviatedIRI="rdfs:comment"/>
        <IRI>#coste_unitario</IRI>
        <Literal datatypeIRI="&rdf;PlainLiteral">Coste del billete sencillo para un trayecto en la línea determinada</Literal>
    </AnnotationAssertion>
    <AnnotationAssertion>
        <AnnotationProperty abbreviatedIRI="rdfs:comment"/>
        <IRI>#descriptor_parada</IRI>
        <Literal datatypeIRI="&rdf;PlainLiteral">Descripción de la parada</Literal>
    </AnnotationAssertion>
    <AnnotationAssertion>
        <AnnotationProperty abbreviatedIRI="rdfs:comment"/>
        <IRI>#dias_aplicables</IRI>
        <Literal datatypeIRI="&rdf;PlainLiteral">Dias a los que se aplica el horario, separados por comas</Literal>
    </AnnotationAssertion>
    </AnnotationAssertion>
    <AnnotationAssertion>
        <AnnotationProperty abbreviatedIRI="rdfs:comment"/>
        <IRI>#fin_tramo_horario</IRI>
        <Literal datatypeIRI="&rdf;PlainLiteral">Hora de fin del tramo horario</Literal>
    </AnnotationAssertion>
    <AnnotationAssertion>
        <AnnotationProperty abbreviatedIRI="rdfs:comment"/>
        <IRI>#frecuencia_de_servicio</IRI>
        <Literal datatypeIRI="&rdf;PlainLiteral">Frecuencia de servicio, expresada en minutos</Literal>
    </AnnotationAssertion>
    <AnnotationAssertion>
        <AnnotationProperty abbreviatedIRI="rdfs:comment"/>
        <IRI>#hora_apertura_parada</IRI>
        <Literal datatypeIRI="&rdf;PlainLiteral">Indica la hora de apertura de la parada de metro (formato HH:MM)</Literal>
    </AnnotationAssertion>
    <AnnotationAssertion>
        <AnnotationProperty abbreviatedIRI="rdfs:comment"/>
        <IRI>#hora_de_cierre_parada</IRI>
        <Literal datatypeIRI="&rdf;PlainLiteral">Indica la hora de apertura de la parada de metro (formato HH:MM)
    </Literal>
    </AnnotationAssertion>
    <AnnotationAssertion>
        <AnnotationProperty abbreviatedIRI="rdfs:comment"/>
        <IRI>#hora_de_inicio</IRI>
        <Literal datatypeIRI="&rdf;PlainLiteral">Hora de inicio de una parada en particular, con formato (HH:MM)</Literal>
    </AnnotationAssertion>
    <AnnotationAssertion>
        <AnnotationProperty abbreviatedIRI="rdfs:comment"/>
        <IRI>#hora_fin</IRI>
        <Literal datatypeIRI="&rdf;PlainLiteral">Hora de finalización del servicio de la línea para un horario concreto, con formato (HH:MM)
    </Literal>
    </AnnotationAssertion>
    <AnnotationAssertion>
        <AnnotationProperty abbreviatedIRI="rdfs:comment"/>
        <IRI>#horario_festivo</IRI>
        <Literal datatypeIRI="&rdf;PlainLiteral">Indica si el horario se refiere a días festivos o no.</Literal>
    </AnnotationAssertion>
    <AnnotationAssertion>
        <AnnotationProperty abbreviatedIRI="rdfs:comment"/>
        <IRI>#inicio_tamo_horario</IRI>
        <Literal datatypeIRI="&rdf;PlainLiteral">Inicio del tramo horario, con el formato &quot;HH:MM&quot;
    </Literal>
    </AnnotationAssertion>
    <AnnotationAssertion>
        <AnnotationProperty abbreviatedIRI="rdfs:comment"/>
        <IRI>#parada_destino</IRI>
        <Literal datatypeIRI="&rdf;PlainLiteral">Parada de destino de la línea</Literal>
    </AnnotationAssertion>
    <AnnotationAssertion>
        <AnnotationProperty abbreviatedIRI="rdfs:comment"/>
        <IRI>#parada_ida</IRI>
        <Literal datatypeIRI="&rdf;PlainLiteral">Indica si la parada de autobús corresponde al trayecto de ida o en caso contrario
    </Literal>
    </AnnotationAssertion>
    <AnnotationAssertion>
        <AnnotationProperty abbreviatedIRI="rdfs:comment"/>
        <IRI>#parada_origen</IRI>
        <Literal datatypeIRI="&rdf;PlainLiteral">Parada de origen de la línea</Literal>
    </AnnotationAssertion>
    <AnnotationAssertion>
        <AnnotationProperty abbreviatedIRI="rdfs:comment"/>
        <IRI>#pertenece_a_estacion</IRI>
        <Literal datatypeIRI="&rdf;PlainLiteral">Indica si la parada pertenece a una estación con más paradas o es una marquesina.</Literal>
    </AnnotationAssertion>
    <AnnotationAssertion>
        <AnnotationProperty abbreviatedIRI="rdfs:comment"/>
        <IRI>#tiene_horario</IRI>
        <Literal datatypeIRI="&rdf;PlainLiteral">Indica un horario en particular de la línea</Literal>
    </AnnotationAssertion>
    <AnnotationAssertion>
        <AnnotationProperty abbreviatedIRI="rdfs:comment"/>
        <IRI>#tiene_paradas_intermedias</IRI>
        <Literal datatypeIRI="&rdf;PlainLiteral">Indica las paradas intermedias de la línea
    </Literal>
    </AnnotationAssertion>
    <AnnotationAssertion>
        <AnnotationProperty abbreviatedIRI="rdfs:comment"/>
        <IRI>#tiene_tarifa</IRI>
        <Literal datatypeIRI="&rdf;PlainLiteral">Tarifa aplicable a la línea
    </Literal>
    <AnnotationAssertion>
        <AnnotationProperty abbreviatedIRI="rdfs:comment"/>
        <IRI>#velocidad_máxima_permitida</IRI>
        <Literal datatypeIRI="&rdf;PlainLiteral">Velocidad máxima permitida del vehículo</Literal>
    </AnnotationAssertion>
    <AnnotationAssertion>
        <AnnotationProperty abbreviatedIRI="rdfs:comment"/>
        <IRI>#zona_tarifaria</IRI>
        <Literal datatypeIRI="&rdf;PlainLiteral">Descriptor de la zona tarifaria de la línea
    </Literal>
    </AnnotationAssertion>
</Ontology>





