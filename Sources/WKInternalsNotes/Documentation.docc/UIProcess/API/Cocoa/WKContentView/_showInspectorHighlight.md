# ``WKInternalsNotes/WKContentView/_showInspectorHighlight(_:)``

インスペクタのハイライト表示を行う。

## Objective-C Declaration
```objective-c
- (void)_showInspectorHighlight:(const WebCore::InspectorOverlay::Highlight&)highlight;
```

## Discussion
`_inspectorHighlightView` が無ければ生成して `rootContentView` の上に追加し、ハイライト情報とズーム倍率/可視領域を渡して更新する。

## References
- [`WKContentView.h#L125`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentView.h#L125)
- [`WKContentView.mm#L613`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentView.mm#L613)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
