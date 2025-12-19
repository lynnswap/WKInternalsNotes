# ``WKInternalsNotes/WKProcessPool/_crashOnMessageCheckFailureForTesting()``

IPC メッセージ検証失敗時にクラッシュする設定を有効化する（テスト用）。

## Objective-C Declaration
```objective-c
+ (void)_crashOnMessageCheckFailureForTesting WK_API_AVAILABLE(macos(15.4), ios(18.4), visionos(2.4));
```

## Discussion
`IPC::Connection::setShouldCrashOnMessageCheckFailure(true)` を呼び出す。

## References
- [`WKProcessPoolPrivate.h#L164`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKProcessPoolPrivate.h#L164)
- [`WKProcessPool.mm#L547`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKProcessPool.mm#L547)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
