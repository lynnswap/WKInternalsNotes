# ``WKInternalsNotes/WKContentView/didInterruptScrolling()``

スクロール中断時の処理を行う。

## Objective-C Declaration
```objective-c
- (void)didInterruptScrolling;
```

## Discussion
`_historicalKinematicData` をクリアする。

## References
- [`WKContentView.h#L87`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentView.h#L87)
- [`WKContentView.mm#L751`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentView.mm#L751)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
