# ``WKInternalsNotes/WKBrowsingContextLoadDelegatePrivate/browsingContextControllerWebProcessDidCrash(_:)``

WebProcess クラッシュ時に通知される delegate フック。

## Objective-C Declaration
```objective-c
- (void)browsingContextControllerWebProcessDidCrash:(WKBrowsingContextController *)sender;
```

## Discussion
`WKBrowsingContextLoadDelegatePrivate` の optional メソッドとして定義されている。対象の `WKBrowsingContextController` が引数で渡される。

## References
- [`WKBrowsingContextLoadDelegatePrivate.h#L36`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKBrowsingContextLoadDelegatePrivate.h#L36)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
