# ``WKInternalsNotes/WKContentView/showingInspectorIndication``

インスペクタ表示インジケータの表示状態を返す/設定する。

## Objective-C Declaration
```objective-c
@property (nonatomic, getter=isShowingInspectorIndication) BOOL showingInspectorIndication;
```

## Default Value
`_inspectorIndicationView` の有無で判定する。

## Discussion
getter は `_inspectorIndicationView` の有無を返す。setter はビュー生成/削除とサブビュー挿入を行う。

## References
- [`WKContentView.h#L62`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentView.h#L62)
- [`WKContentView.mm#L630`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentView.mm#L630)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
