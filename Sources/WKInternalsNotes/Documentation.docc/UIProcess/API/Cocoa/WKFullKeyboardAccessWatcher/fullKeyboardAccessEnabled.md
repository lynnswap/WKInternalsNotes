# ``WKInternalsNotes/WKFullKeyboardAccessWatcher/fullKeyboardAccessEnabled()``

フルキーボードアクセスの有効状態を返す。

## Objective-C Declaration
```objective-c
+ (BOOL)fullKeyboardAccessEnabled;
```

## Discussion
静的に保持した `WKFullKeyboardAccessWatcher` を生成し、内部の `fullKeyboardAccessEnabled` を返す。インスタンス生成時に通知監視を開始するため、この値は通知更新された最新状態を保持する。

## References
- [`WKFullKeyboardAccessWatcher.h#L32`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/Cocoa/WKFullKeyboardAccessWatcher.h#L32)
- [`WKFullKeyboardAccessWatcher.mm#L107`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/Cocoa/WKFullKeyboardAccessWatcher.mm#L107)
- [`WKFullKeyboardAccessWatcher.mm#L109`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/Cocoa/WKFullKeyboardAccessWatcher.mm#L109)
- [`WKFullKeyboardAccessWatcher.mm#L110`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/Cocoa/WKFullKeyboardAccessWatcher.mm#L110)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-20 |
