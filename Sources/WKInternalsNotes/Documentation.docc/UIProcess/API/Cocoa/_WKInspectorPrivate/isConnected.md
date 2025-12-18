# ``WKInternalsNotes/_WKInspector/isConnected``

インスペクタのフロントエンドページが作成済みかどうかを返す。

## Objective-C Declaration
```objective-c
@property (nonatomic, readonly) BOOL isConnected;
```

## Default Value
`false`（`m_inspectorPage` が `nil` の初期状態）

## Discussion
`WebInspectorUIProxy::isConnected()` は `m_inspectorPage` の有無で判定する。`connect` は `createFrontendPage()` を呼ぶため、フロントエンド作成後に `true` になる。

## References
- [`_WKInspector.h#L46`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKInspector.h#L46)
- [`_WKInspector.mm#L115`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKInspector.mm#L115)
- [`WebInspectorUIProxy.h#L133`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/Inspector/WebInspectorUIProxy.h#L133)
- [`WebInspectorUIProxy.cpp#L143`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/Inspector/WebInspectorUIProxy.cpp#L143)
- [`WebInspectorUIProxy.cpp#L447`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/Inspector/WebInspectorUIProxy.cpp#L447)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
