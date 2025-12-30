# ``WKInternalsNotes/_WKUserInitiatedAction/consume()``

ユーザー操作を消費済みにする。

## Objective-C Declaration
```objective-c
- (void)consume;
```

## Discussion
内部の `API::UserInitiatedAction` に `setConsumed()` を呼び出して消費済み状態へ変更する。

## References
- [`_WKUserInitiatedAction.h#L35`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKUserInitiatedAction.h#L35)
- [`_WKUserInitiatedAction.mm#L56`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKUserInitiatedAction.mm#L56)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |
