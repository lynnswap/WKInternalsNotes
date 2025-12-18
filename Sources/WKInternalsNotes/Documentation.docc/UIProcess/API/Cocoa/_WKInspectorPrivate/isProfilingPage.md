# ``WKInternalsNotes/_WKInspector/isProfilingPage``

ページプロファイリングの実行状態を返す。

## Objective-C Declaration
```objective-c
@property (nonatomic, readonly) BOOL isProfilingPage;
```

## Default Value
`false`（`m_isProfilingPage` の初期値）

## Discussion
`togglePageProfiling` は現在の状態に応じて Start/Stop を送信し、状態自体は `timelineRecordingChanged` で更新される。

## References
- [`_WKInspector.h#L49`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKInspector.h#L49)
- [`_WKInspector.mm#L130`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKInspector.mm#L130)
- [`WebInspectorUIProxy.h#L201`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/Inspector/WebInspectorUIProxy.h#L201)
- [`WebInspectorUIProxy.h#L343`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/Inspector/WebInspectorUIProxy.h#L343)
- [`WebInspectorUIProxy.cpp#L402`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/Inspector/WebInspectorUIProxy.cpp#L402)
- [`WebInspectorUIProxy.cpp#L777`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/Inspector/WebInspectorUIProxy.cpp#L777)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
