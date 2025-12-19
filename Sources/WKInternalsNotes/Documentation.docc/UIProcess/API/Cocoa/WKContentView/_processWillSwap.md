# ``WKInternalsNotes/WKContentView/_processWillSwap()``

Webプロセスのスワップ前に後処理を行う。

## Objective-C Declaration
```objective-c
- (void)_processWillSwap;
```

## Discussion
現状は `_processDidExit` を呼び出して同等の後処理を実施する。

## References
- [`WKContentView.h#L105`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentView.h#L105)
- [`WKContentView.mm#L933`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentView.mm#L933)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
