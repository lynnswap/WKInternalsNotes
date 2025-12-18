# ``WKInternalsNotes/WKNavigationResponse/_frame``

レスポンスのフレーム情報を返す。

## Objective-C Declaration
```objective-c
@property (nonatomic, readonly) WKFrameInfo *_frame;
```

## Default Value
`_navigationResponse->protectedFrame()` をラップした `WKFrameInfo`。

## Discussion
clang static analyzer 対策の `RefPtr` を経由して `protectedFrame()` を取り出し、`wrapper(...)` で Objective-C ラッパーに変換して返す。

## References
- [`WKNavigationResponsePrivate.h#L31`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKNavigationResponsePrivate.h#L31)
- [`WKNavigationResponse.mm#L78`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKNavigationResponse.mm#L78)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
