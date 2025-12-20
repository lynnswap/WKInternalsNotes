# ``WKInternalsNotes/_WKApplicationManifest/manifestId``

マニフェスト ID の URL を返す。

## Objective-C Declaration
```objective-c
@property (nonatomic, readonly, copy) NSURL *manifestId WK_API_AVAILABLE(macos(13.3), ios(16.4));
```

## Discussion
`ApplicationManifest` の `id` を `NSURL` に変換して返す。

## References
- [`_WKApplicationManifest.h#L84`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKApplicationManifest.h#L84)
- [`_WKApplicationManifest.mm#L498`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKApplicationManifest.mm#L498)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-20 |
