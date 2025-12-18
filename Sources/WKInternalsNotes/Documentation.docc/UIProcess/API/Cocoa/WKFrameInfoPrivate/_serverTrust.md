# ``WKInternalsNotes/WKFrameInfo/_serverTrust``

フレームの証明書情報に対応する SecTrustRef を返す。

## Objective-C Declaration
```objective-c
@property (nonatomic, readonly, nullable) SecTrustRef _serverTrust WK_API_AVAILABLE(macos(26.0), ios(26.0), visionos(26.0));
```

## Default Value
`frameInfoData().certificateInfo.trust().get()` の結果。

## Discussion
`certificateInfo.trust()` の `SecTrustRef` をそのまま返す。値が無い場合は `nil` になる。

## References
- [`WKFrameInfoPrivate.h#L46`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKFrameInfoPrivate.h#L46)
- [`WKFrameInfo.mm#L160`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKFrameInfo.mm#L160)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
