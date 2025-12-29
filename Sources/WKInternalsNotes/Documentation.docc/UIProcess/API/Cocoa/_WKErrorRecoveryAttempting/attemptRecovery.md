# ``WKInternalsNotes/_WKErrorRecoveryAttempting/attemptRecovery()``

エラー回復のためにフレーム再読み込みを試みる。

## Objective-C Declaration
```objective-c
- (BOOL)attemptRecovery;
```

## Discussion
`WKReloadFrameErrorRecoveryAttempter` では `WKWebView` と `WebFrameProxy` が存在する場合に、保持している URL を再読み込みして `YES` を返す。いずれかが取得できない場合は `NO` を返す。

## References
- [`WKReloadFrameErrorRecoveryAttempter.mm#L60`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/Cocoa/WKReloadFrameErrorRecoveryAttempter.mm#L60)
- [`_WKErrorRecoveryAttempting.h#L34`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKErrorRecoveryAttempting.h#L34)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-29 |
