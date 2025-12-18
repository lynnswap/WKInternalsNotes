# ``WKInternalsNotes/WKBrowsingContextLoadDelegatePrivate/browsingContextController(_:canAuthenticateAgainstProtectionSpace:)``

認証空間に対する認証可否を問い合わせる delegate フック。

## Objective-C Declaration
```objective-c
- (BOOL)browsingContextController:(WKBrowsingContextController *)sender canAuthenticateAgainstProtectionSpace:(NSURLProtectionSpace *)protectionSpace;
```

## Discussion
`WKBrowsingContextLoadDelegatePrivate` の optional メソッドとして定義されている。戻り値の `BOOL` で認証可能かどうかを示すインターフェース。

## References
- [`WKBrowsingContextLoadDelegatePrivate.h#L33`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKBrowsingContextLoadDelegatePrivate.h#L33)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
