# ``WKInternalsNotes/WKWebViewConfiguration/_allowPostingLegacySynchronousMessages``

legacy synchronous message の投稿を許可

## Objective-C Declaration
```objective-c
@property (nonatomic, setter=_setAllowPostingLegacySynchronousMessages:) BOOL _allowPostingLegacySynchronousMessages WK_API_AVAILABLE(macos(WK_MAC_TBA), ios(WK_IOS_TBA));
```

## Default Value
iOS: `NO` / macOS: `NO`

## Discussion
- この API を使わない場合: 既定値のまま動作する。
- `_allowPostingLegacySynchronousMessages = YES`: legacy synchronous message の投稿を許可。
- `_allowPostingLegacySynchronousMessages = NO`: legacy synchronous message の投稿を許可（無効）。

## Details
- setter は呼び出し元 bundle id を `RELEASE_ASSERT` で制限

## References
- [`WKWebViewConfigurationPrivate.h#L100`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewConfigurationPrivate.h#L100)
- [`WKWebViewConfiguration.mm#L680`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewConfiguration.mm#L680)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-16 |
