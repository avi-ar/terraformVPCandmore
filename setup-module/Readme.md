<mxfile host="app.diagrams.net" modified="2023-07-03T11:39:09.771Z" agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36" etag="TV53Prlb8jW3y31G_WLF" version="21.3.3" type="device">
  <diagram name="Page-1" id="GtFMFcPw0Rscw-Qx1ujX">
    <mxGraphModel dx="1434" dy="1900" grid="1" gridSize="10" guides="1" tooltips="1" connect="1" arrows="1" fold="1" page="1" pageScale="1" pageWidth="850" pageHeight="1100" math="0" shadow="0">
      <root>
        <mxCell id="0" />
        <mxCell id="1" parent="0" />
        <mxCell id="39Jxf6Hnct3Z94-lEbiL-2" value="" style="whiteSpace=wrap;html=1;aspect=fixed;" vertex="1" parent="1">
          <mxGeometry x="270" y="-260" width="780" height="780" as="geometry" />
        </mxCell>
        <mxCell id="39Jxf6Hnct3Z94-lEbiL-17" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;" edge="1" parent="1" source="39Jxf6Hnct3Z94-lEbiL-3" target="39Jxf6Hnct3Z94-lEbiL-12">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>
        <mxCell id="39Jxf6Hnct3Z94-lEbiL-3" value="" style="outlineConnect=0;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=center;html=1;shape=mxgraph.aws3.virtual_private_cloud;fillColor=#F58534;gradientColor=none;" vertex="1" parent="1">
          <mxGeometry x="270" y="-260" width="79.5" height="54" as="geometry" />
        </mxCell>
        <mxCell id="39Jxf6Hnct3Z94-lEbiL-8" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;" edge="1" parent="1" source="39Jxf6Hnct3Z94-lEbiL-4" target="39Jxf6Hnct3Z94-lEbiL-7">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>
        <mxCell id="39Jxf6Hnct3Z94-lEbiL-4" value="lambda func that using event bridge scheduler stop the machine at 19&amp;nbsp;" style="outlineConnect=0;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=center;html=1;shape=mxgraph.aws3.lambda_function;fillColor=#F58534;gradientColor=none;" vertex="1" parent="1">
          <mxGeometry x="800" y="40" width="69" height="72" as="geometry" />
        </mxCell>
        <mxCell id="39Jxf6Hnct3Z94-lEbiL-9" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;" edge="1" parent="1" source="39Jxf6Hnct3Z94-lEbiL-5" target="39Jxf6Hnct3Z94-lEbiL-7">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>
        <mxCell id="39Jxf6Hnct3Z94-lEbiL-5" value="lambda func that using event bridge scheduler starts the machine at 7&amp;nbsp;" style="outlineConnect=0;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=center;html=1;shape=mxgraph.aws3.lambda_function;fillColor=#F58534;gradientColor=none;" vertex="1" parent="1">
          <mxGeometry x="800" y="410" width="69" height="72" as="geometry" />
        </mxCell>
        <mxCell id="39Jxf6Hnct3Z94-lEbiL-14" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;" edge="1" parent="1" source="39Jxf6Hnct3Z94-lEbiL-6" target="39Jxf6Hnct3Z94-lEbiL-13">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>
        <mxCell id="39Jxf6Hnct3Z94-lEbiL-16" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;entryX=0.692;entryY=0.038;entryDx=0;entryDy=0;entryPerimeter=0;" edge="1" parent="1" source="39Jxf6Hnct3Z94-lEbiL-6" target="39Jxf6Hnct3Z94-lEbiL-15">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>
        <mxCell id="39Jxf6Hnct3Z94-lEbiL-6" value="EC2 MACHINE THAT RUNS ANSIBLE AND JENKINS SERVER" style="sketch=0;points=[[0,0,0],[0.25,0,0],[0.5,0,0],[0.75,0,0],[1,0,0],[0,1,0],[0.25,1,0],[0.5,1,0],[0.75,1,0],[1,1,0],[0,0.25,0],[0,0.5,0],[0,0.75,0],[1,0.25,0],[1,0.5,0],[1,0.75,0]];outlineConnect=0;fontColor=#232F3E;gradientColor=#F78E04;gradientDirection=north;fillColor=#D05C17;strokeColor=#ffffff;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=center;html=1;fontSize=12;fontStyle=0;aspect=fixed;shape=mxgraph.aws4.resourceIcon;resIcon=mxgraph.aws4.ec2;" vertex="1" parent="1">
          <mxGeometry x="580" y="230" width="78" height="78" as="geometry" />
        </mxCell>
        <mxCell id="39Jxf6Hnct3Z94-lEbiL-10" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;" edge="1" parent="1" source="39Jxf6Hnct3Z94-lEbiL-7" target="39Jxf6Hnct3Z94-lEbiL-6">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>
        <mxCell id="39Jxf6Hnct3Z94-lEbiL-7" value="" style="sketch=0;points=[[0,0,0],[0.25,0,0],[0.5,0,0],[0.75,0,0],[1,0,0],[0,1,0],[0.25,1,0],[0.5,1,0],[0.75,1,0],[1,1,0],[0,0.25,0],[0,0.5,0],[0,0.75,0],[1,0.25,0],[1,0.5,0],[1,0.75,0]];outlineConnect=0;fontColor=#232F3E;gradientColor=#FF4F8B;gradientDirection=north;fillColor=#BC1356;strokeColor=#ffffff;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=center;html=1;fontSize=12;fontStyle=0;aspect=fixed;shape=mxgraph.aws4.resourceIcon;resIcon=mxgraph.aws4.eventbridge;" vertex="1" parent="1">
          <mxGeometry x="840" y="250" width="50" height="50" as="geometry" />
        </mxCell>
        <mxCell id="39Jxf6Hnct3Z94-lEbiL-12" value="Vpc that is on the 10.0.0.0/16 network has 3 private sub nets and 3 public ones&amp;nbsp;&amp;nbsp;" style="rounded=1;whiteSpace=wrap;html=1;" vertex="1" parent="1">
          <mxGeometry x="270" y="-170" width="120" height="60" as="geometry" />
        </mxCell>
        <mxCell id="39Jxf6Hnct3Z94-lEbiL-13" value="internet gatewat" style="outlineConnect=0;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=center;html=1;shape=mxgraph.aws3.internet_gateway;fillColor=#F58536;gradientColor=none;" vertex="1" parent="1">
          <mxGeometry x="610.5" y="-290" width="69" height="72" as="geometry" />
        </mxCell>
        <mxCell id="39Jxf6Hnct3Z94-lEbiL-15" value="Security group which contains the following rules&amp;nbsp;&lt;br&gt;ingress:22,8080,80&lt;br&gt;egress:wide open(from port 0 to port 0 in the tf file" style="fillColor=none;strokeColor=#DD3522;verticalAlign=top;fontStyle=0;fontColor=#DD3522;whiteSpace=wrap;html=1;" vertex="1" parent="1">
          <mxGeometry x="520" y="340" width="130" height="130" as="geometry" />
        </mxCell>
      </root>
    </mxGraphModel>
  </diagram>
</mxfile>
# TerraformVpc
