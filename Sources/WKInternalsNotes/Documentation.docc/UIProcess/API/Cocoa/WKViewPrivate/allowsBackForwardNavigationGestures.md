# ``WKInternalsNotes/WKView/allowsBackForwardNavigationGestures``

戻る/進むジェスチャを許可するか返す。

## Objective-C Declaration
```objective-c
@property (readwrite) BOOL allowsBackForwardNavigationGestures;
```

## Default Value
`NO`。

## Discussion
getter は `NO` を返し、setter は空実装。

## References
- [`WKViewPrivate.h#L69`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKViewPrivate.h#L69)
- [`WKView.mm#L1146`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/mac/WKView.mm#L1146)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
