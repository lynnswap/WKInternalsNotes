# ``WKInternalsNotes/_WKWebContentProcessInfo/webContentState``

WebContentProcess の状態（prewarmed / cached / active）を返す。

## Objective-C Declaration
```objective-c
@property (nonatomic, readonly) _WKWebContentProcessState webContentState;
```

## Default Value
既定は `_WKWebContentProcessStateActive` だが、`process.isPrewarmed()` または `process.isInProcessCache()` に応じて上書きされる。

## Discussion
初期化時に `WebProcessProxy` の状態から `webContentState` を決定する。

## References
- [`WKProcessPoolPrivate.h#L65`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKProcessPoolPrivate.h#L65)
- [`WKProcessPool.mm#L801`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKProcessPool.mm#L801)
- [`WKProcessPool.mm#L802`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKProcessPool.mm#L802)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-20 |
