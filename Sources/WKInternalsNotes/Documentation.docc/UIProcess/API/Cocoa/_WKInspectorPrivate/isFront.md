# ``WKInternalsNotes/_WKInspector/isFront``

インスペクタ UI が前面にあるかどうかを返す。

## Objective-C Declaration
```objective-c
@property (nonatomic, readonly) BOOL isFront;
```

## Default Value
`false`（検査対象ページが無い場合）

## Discussion
`WebInspectorUIProxy::isFront()` は検査対象ページが無い場合に `false` を返し、存在する場合はプラットフォーム実装の前面判定に委譲する。

## References
- [`_WKInspector.h#L48`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKInspector.h#L48)
- [`_WKInspector.mm#L125`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKInspector.mm#L125)
- [`WebInspectorUIProxy.cpp#L135`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/Inspector/WebInspectorUIProxy.cpp#L135)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
