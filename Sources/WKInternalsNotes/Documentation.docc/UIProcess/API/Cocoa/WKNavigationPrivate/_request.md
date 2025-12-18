# ``WKInternalsNotes/WKNavigation/_request``

ナビゲーション開始時の元リクエストを返す。

## Objective-C Declaration
```objective-c
@property (nonatomic, readonly, copy) NSURLRequest *_request;
```

## Default Value
`_navigation->originalRequest().nsURLRequest(WebCore::HTTPBodyUpdatePolicy::DoNotUpdateHTTPBody)` の結果。

## Discussion
`originalRequest()` の `NSURLRequest` を生成し、HTTP body を更新しないポリシーで返す。

## References
- [`WKNavigationPrivate.h#L32`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKNavigationPrivate.h#L32)
- [`WKNavigation.mm#L53`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKNavigation.mm#L53)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
