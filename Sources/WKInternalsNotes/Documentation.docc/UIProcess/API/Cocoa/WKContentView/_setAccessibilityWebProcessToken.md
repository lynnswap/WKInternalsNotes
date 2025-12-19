# ``WKInternalsNotes/WKContentView/_setAccessibilityWebProcessToken(_:)``

Webプロセスのアクセシビリティトークン受信を反映する。

## Objective-C Declaration
```objective-c
- (void)_setAccessibilityWebProcessToken:(NSData *)data;
```

## Discussion
Webプロセスがチェックインしたことを契機に、UIプロセス側のアクセシビリティ登録を更新する。

## References
- [`WKContentView.h#L131`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentView.h#L131)
- [`WKContentView.mm#L834`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentView.mm#L834)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
