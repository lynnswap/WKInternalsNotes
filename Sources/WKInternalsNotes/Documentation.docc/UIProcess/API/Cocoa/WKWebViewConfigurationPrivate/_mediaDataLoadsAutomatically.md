# ``WKInternalsNotes/WKWebViewConfiguration/_mediaDataLoadsAutomatically``

media data を自動ロード

## Objective-C Declaration
```objective-c
@property (nonatomic, setter=_setMediaDataLoadsAutomatically:) BOOL _mediaDataLoadsAutomatically WK_API_AVAILABLE(macos(10.12), ios(10.0));
```

## Default Value
iOS: `!PAL::currentUserInterfaceIdiomIsSmallScreen()` / macOS: `YES`

## Discussion
- この API を使わない場合: 既定値のまま動作する。
- `_mediaDataLoadsAutomatically = YES`: media data を自動ロード。
- `_mediaDataLoadsAutomatically = NO`: media data を自動ロード（無効）。

## Details
- iOS は UI idiom 依存（概ね iPhone: `NO`, iPad: `YES`）

## References
- [`WKWebViewConfigurationPrivate.h#L85`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewConfigurationPrivate.h#L85)
- [`WKWebViewConfiguration.mm#L1007`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewConfiguration.mm#L1007)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-16 |
