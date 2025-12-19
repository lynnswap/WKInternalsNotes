# ``WKInternalsNotes/WKContentView/_closeCurrentTypingCommand()``

現在のタイピングコマンドを閉じる。

## Objective-C Declaration
```objective-c
- (void)_closeCurrentTypingCommand;
```

## Discussion
`_page` が存在する場合に `WebPageProxy::closeCurrentTypingCommand()` を呼び出す。

## References
- [`WKContentViewInteraction.h#L1001`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.h#L1001)
- [`WKContentViewInteraction.mm#L14208`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.mm#L14208)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
